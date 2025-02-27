from collections import defaultdict
from functools import lru_cache
from math import sqrt

def is_prime(n: int) -> bool:
    if not n % 2 and n != 2:
        return False
    return all((n % i for i in range(3, int(sqrt(n)) + 1, 2)))

@lru_cache(maxsize=None)
def is_truncatable(n: int) -> bool:
    if is_prime(n):
        if '0' in str(n):
            return False
        if len(str(n)) < 3:
            return True
        for r in range(0, len(str(n))):
            new_value = int(str(n)[r:])
            if new_value in PRIMES:
                if r == len(str(n)) - 1:
                    return True
                continue
            new_value = int(str(n)[:-r])
            if new_value in PRIMES:
                if r == 0:
                    return True
    return False

@lru_cache(maxsize=None)
def find_truncable_primes(n: int) -> set:
    return {k for k in PRIMES if k <= n and is_truncatable(k)}

def all_left_right_truncatable_prime(digits: tuple) -> list:
    x = digits[38]
    return sorted(find_truncable_primes(x), reverse=True)