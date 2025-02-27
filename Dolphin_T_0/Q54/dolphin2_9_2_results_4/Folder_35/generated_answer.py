import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    primes = [i for i in range(x) if is_prime(i) and is_prime(int(str(i)[-1:]))]
    right_truncatable_primes = []
    for prime in primes:
        while prime > 0 and is_prime(prime):
            right_truncatable_primes.append(prime)
            prime = int(str(prime)[:-1])
    return sorted(right_truncatable_primes)