from sympy import isprime

def all_right_truncatable_prime(args):
    x = args[3]
    rtp = []
    for num in range(1, x):
        num_str = str(num)
        while num_str:
            if not isprime(int(num_str)):
                break
            num_str = num_str[:-1]
        else:
            rtp.append(num)
    return sorted(rtp, reverse=True)