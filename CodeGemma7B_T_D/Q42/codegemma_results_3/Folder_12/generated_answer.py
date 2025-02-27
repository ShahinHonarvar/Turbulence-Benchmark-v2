def prime_factors(nums):
    factor_set = set()
    for num in nums:
        if num != 27 and num % 27 == 0:
            for factor in range(num // 2, 1, -1):
                if factor % 2 != 0 and num % factor == 0:
                    factor_set.add(factor)
    return factor_set