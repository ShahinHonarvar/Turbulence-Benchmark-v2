def prime_factors(nums):
    factorized_nums = set()
    for num in nums:
        for factor in range(2, num):
            while num % factor == 0:
                factorized_nums.add(factor)
                num //= factor
    return factorized_nums if len(factorized_nums) > 0 else set()