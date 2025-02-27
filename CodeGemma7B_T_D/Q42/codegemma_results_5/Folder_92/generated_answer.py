def prime_factors(nums):
    factors = set()
    for factor in range(2, nums[0] + 1):
        while nums[0] % factor == 0:
            nums[0] /= factor
            factors.add(factor)
    return factors