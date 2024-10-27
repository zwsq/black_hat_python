import socket
import datetime

def port_scanner(ip, port):
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print(f"[!] Port {port} is open.")
    except:
        None

def main():
    target_ip=input("[~] What is target IP address? ")
    target_port=input("[~]Enter port number range(separated by comma ','): ")
    target_port_range=target_port.split(',')
    print(f"[~] Scanning {target_ip}")
    start_time=datetime.datetime.now()

    for x in range(int(target_port_range[0]), int(target_port_range[1])):
        port_scanner(target_ip, x)

    end_time=datetime.datetime.now()
    scan_duration = end_time - start_time
    print(f"scanned {int(target_port_range[1]) - int(target_port_range[0])} ports in {scan_duration.seconds} seconds.")

if __name__ == "__main__":
    main()