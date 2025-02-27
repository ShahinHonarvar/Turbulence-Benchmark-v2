from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_left_truncatable_prime(x):
    primes = [i for i in range(1, x) if is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)