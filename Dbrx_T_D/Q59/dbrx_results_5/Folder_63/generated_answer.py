from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes():
    for i in count(1):
        if is_prime(i) and '0' not in str(i):
            yield i

def all_left_truncatable_prime(t):
    x = t[88]
    return sorted((i for i in left_truncatable_primes() if i < x))