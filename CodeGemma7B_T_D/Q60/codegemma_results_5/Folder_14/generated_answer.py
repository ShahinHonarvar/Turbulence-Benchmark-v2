from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def has_zero(n):
    return '0' in str(n)

def is_truncatable_prime(n):
    if has_zero(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[78]
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes