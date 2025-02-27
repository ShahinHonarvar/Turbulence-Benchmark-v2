import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[33]
    primes = [i for i in range(2, x) if is_prime(i)]

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n % 100
        return True
    return sorted(filter(is_left_truncatable_prime, primes))