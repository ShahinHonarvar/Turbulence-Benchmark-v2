from math import sqrt

def prime_factors(nums):
    return {f for num in nums for f in prime_factors_set(num) if f not in (1, num)}

def prime_factors_set(num):
    factors = set()
    for n in range(2, int(sqrt(num)) + 1):
        while num % n == 0:
            factors.add(n)
            num //= n
    if num > 1:
        factors.add(num)
    return factors