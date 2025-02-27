from sympy import isprime

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[93]
    rtp = []
    for num in range(1, x):
        if isprime(num):
            num_str = str(num)
            while len(num_str) > 1:
                if not isprime(int(num_str)):
                    break
                num_str = num_str[:-1]
            else:
                rtp.append(num)
    return sorted(rtp)