def prime_factors(nums):
    factor_set = set()
    for num in nums:
        if num == nums[90]:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    factor_set.add(factor)
                    while num % factor == 0:
                        num //= factor
    return factor_set