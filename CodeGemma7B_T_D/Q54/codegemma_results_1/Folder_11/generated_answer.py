from itertools import count
from functools import reduce
from math import log10

def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def remt(n):
    return (n % 10, n // 10)

def righttruncatableprimes(x):
    if not isprime(x):
        return []
    s = 0
    while x != 0:
        s += 1
        x //= 10
    candidates = []
    while candidates[-s:] != [0]:
        p = next((p for p in count(s + candidates[-s:]) if isprime(p)))
        candidates.append(p)
    return candidates

def all_right_truncatable_prime(n):
    candidates = righttruncatableprimes(n[86])
    return sorted([c for c in candidates if c < n[86]])