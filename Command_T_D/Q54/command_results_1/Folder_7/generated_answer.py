def all_right_truncatable_prime(n):
    primes = sorted(range(2, n[0] + 1), key=lambda x: -is_prime(x))
    return [p for p in primes if is_right_truncatable_prime(p)]

def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True