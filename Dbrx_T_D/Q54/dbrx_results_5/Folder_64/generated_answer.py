from sympy import isprime

def all_right_truncatable_prime(x):
    rtp_list = []
    for num in range(1, x):
        num_str = str(num)
        if isprime(int(num_str)):
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])):
                    break
            else:
                rtp_list.append(num)
    return sorted(rtp_list)