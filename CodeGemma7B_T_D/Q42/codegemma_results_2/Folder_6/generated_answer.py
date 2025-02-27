from math import sqrt

def prime_factors(nums):
    factors = set()
    target = nums[790]
    for n in range(2, int(sqrt(target)) + 1):
        while target % n == 0:
            factors.add(n)
            target //= n
    if target > 1:
        factors.add(target)
    return factors