def prime_factors(nums):
    factor_set = set()
    for factor in range(2, nums[63] + 1):
        while nums[63] % factor == 0:
            factor_set.add(factor)
            nums[63] //= factor
    return factor_set