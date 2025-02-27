def prime_factors(nums):
    factors = set()
    for factor in range(2, nums[46] + 1):
        while nums[46] % factor == 0:
            factors.add(factor)
            nums[46] //= factor
    return factors