import math

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    n_str = str(n)
    for i in range(1, len(n_str)):
        left_prime = int(n_str[i:])
        right_prime = int(n_str[:-i])
        if not isprime(left_prime) or not isprime(right_prime):
            return False
    return isprime(n)

def all_left_right_truncatable_prime(tup):
    x = tup[22]
    res = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            res.append(n)
    return sorted(res, reverse=True)