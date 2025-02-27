from math import sqrt
from functools import reduce
from itertools import count

def next_prime(prime):
    return next((p for p in count(prime + 2, 2) if not any((p % d == 0 for d in range(3, int(sqrt(p)) + 1, 2)))))

def left_truncatable(prime):
    digits = len(str(prime))
    for d in range(1, digits):
        prime = int(str(prime)[:-d])
        if not is_prime(prime):
            return False
    return True

def right_truncatable(prime):
    digits = len(str(prime))
    for d in range(1, digits):
        prime = int(str(prime)[d:])
        if not is_prime(prime):
            return False
    return True

def divisor_count(n):
    if n == 1:
        return 1
    return reduce(lambda accum, x: accum + x, (int(n / d) for d in range(2, int(sqrt(n)) + 1) if n % d == 0), 0) + 2

def is_prime(n):
    if n <= 1 or (n <= 3 and n % 2 != 0):
        return True
    elif n % 6 not in (1, 5):
        return False
    return not divisor_count(n) > 2

def all_left_right_truncatable_prime(x):
    prime = 2
    truncatable_primes = []
    while prime <= x:
        if is_prime(prime) and left_truncatable(prime) and right_truncatable(prime):
            truncatable_primes.append(prime)
        prime = next_prime(prime)
    return sorted(truncatable_primes)