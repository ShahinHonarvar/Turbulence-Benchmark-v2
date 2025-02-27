def prime_factors(nums):
    factor_set = set()
    for num in nums:
        if num == nums[69]:
            for factor in range(2, num + 1):
                if num % factor == 0:
                    factor_set.add(factor)
    return factor_set