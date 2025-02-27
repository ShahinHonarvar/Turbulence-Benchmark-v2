from math import sqrt

def prime_factors(nums):
    prime_factors = set()
    target = nums[459]
    for i in range(2, int(sqrt(target)) + 1):
        while target % i == 0:
            prime_factors.add(i)
            target //= i
    if target > 1:
        prime_factors.add(target)
    return prime_factors