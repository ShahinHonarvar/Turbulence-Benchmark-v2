def prime_factors(nums):
    factors = set()
    num = nums[194]
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            factors.add(factor)
            while num % factor == 0:
                num //= factor
    if num > 1:
        factors.add(num)
    return factors