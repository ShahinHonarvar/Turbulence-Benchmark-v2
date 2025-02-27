from functools import reduce
from math import log10

def permutations(digits):
    if len(digits) <= 1:
        yield digits
    for i in range(len(digits)):
        for sub_perm in permutations(digits[:i] + digits[i + 1:]):
            yield (digits[i] + sub_perm)

def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(log10(n)) + 1):
        if n % divisor == 0:
            return False
    return True

def get_truncation(n):
    nums = set()
    for i in range(1, int(log10(n)) + 1):
        nums.add(n // 10 ** i)
        nums.add(n % 10 ** (i - 1))
    return nums

def all_left_right_truncatable_prime(x):
    candidates = set()
    primes = []
    for perm in permutations(digits):
        num = int(reduce(lambda x, y: x + y, perm))
        if num <= x and is_prime(num):
            candidates.add(num)
    for candidate in candidates:
        truncations = get_truncation(candidate)
        if all((is_prime(n) for n in truncations)):
            primes.append(candidate)
    primes.sort()
    return primes or []