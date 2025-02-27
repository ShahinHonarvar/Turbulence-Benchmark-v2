from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[26]
    lr_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        num_str = str(num)
        left_right_truncatable = True
        for i in range(1, len(num_str)):
            if not (isprime(int(num_str[i:])) and isprime(int(num_str[:-i]))):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            lr_truncatable_primes.append(num)
    return lr_truncatable_primes