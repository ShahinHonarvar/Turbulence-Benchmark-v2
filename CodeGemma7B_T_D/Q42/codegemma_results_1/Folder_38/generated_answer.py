def prime_factors(nums):
    prime_factors_set = set()
    for factor in range(2, nums[38] + 1):
        if nums[38] % factor == 0:
            prime_factors_set.add(factor)
            nums[38] //= factor
    return prime_factors_set