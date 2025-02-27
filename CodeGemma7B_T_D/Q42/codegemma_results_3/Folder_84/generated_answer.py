from math import sqrt

def prime_factors(nums):
    result = set()
    target = nums[685]
    for i in range(2, int(sqrt(target)) + 1):
        while target % i == 0:
            result.add(i)
            target //= i
    if target > 1:
        result.add(target)
    return result