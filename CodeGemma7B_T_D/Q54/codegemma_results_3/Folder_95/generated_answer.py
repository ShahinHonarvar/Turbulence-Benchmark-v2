from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_truncation(n):
    truncation = n % 10
    return truncation

def is_right_truncatable_prime(n):
    while n > 0:
        truncation = get_truncation(n)
        if not is_prime(truncation):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(x):
    truncatable_primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            truncatable_primes.append(n)
    truncatable_primes.sort()
    return truncatable_primes