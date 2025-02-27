def prime_factors(nums):
    factors = set()
    for factor in range(2, nums[46] + 1):
        if nums[46] % factor == 0:
            factors.add(factor)
            while nums[46] % factor == 0:
                nums[46] //= factor
    return factors