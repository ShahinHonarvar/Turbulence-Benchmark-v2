def prime_factors(nums):
    factors = set()
    targetIndex = 321
    targetNumber = nums[targetIndex]
    for factor in range(2, targetNumber + 1):
        while targetNumber % factor == 0:
            factors.add(factor)
            targetNumber //= factor
    return factors