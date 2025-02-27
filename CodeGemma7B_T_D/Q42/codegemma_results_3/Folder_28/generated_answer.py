def prime_factors(nums):
    factor_set = set()
    num = nums[37]
    for factor in range(2, int(num ** 0.5) + 1):
        while num % factor == 0:
            factor_set.add(factor)
            num //= factor
    return factor_set