import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_suffix_prime(n):
    if is_prime(n):
        return is_suffix_prime(n // 10)
    return n == 0

def all_right_truncatable_prime(a_tuple):
    x = a_tuple[8]
    primes = []
    for n in range(x, 0, -1):
        if is_prime(n) and is_suffix_prime(n):
            primes.append(n)
    return primes