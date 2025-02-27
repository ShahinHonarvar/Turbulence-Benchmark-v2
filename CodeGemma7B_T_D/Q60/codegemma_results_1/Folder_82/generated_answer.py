from math import sqrt

def all_left_right_truncatable_prime(x):
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_prime(n) and has_no_zero(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def has_no_zero(n):
    while n >= 10:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:i]))):
            return False
    return True