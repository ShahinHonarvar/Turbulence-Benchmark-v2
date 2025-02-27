from math import sqrt

def smallest_factor(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

def is_prime(n):
    if n <= 1:
        return False
    return smallest_factor(n) == n

def is_right_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:-i])):
            return False
    return is_prime(n)

def all_right_truncatable_primes(t):
    x = t[433]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)