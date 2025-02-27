from math import sqrt
from collections import defaultdict

def prime_factors(nums):
    factorizations = defaultdict(list)
    for num in nums:
        for factor in range(2, int(sqrt(num)) + 1):
            if num % factor == 0:
                factorizations[num].append(factor)
                while num % factor == 0:
                    num //= factor
        if num > 1:
            factorizations[num].append(num)
    return set(factorizations[nums[4]])