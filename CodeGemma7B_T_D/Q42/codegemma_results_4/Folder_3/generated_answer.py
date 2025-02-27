def prime_factors(nums):
    num = nums[100]
    factors = set()
    for factor in range(2, int(num ** 0.5) + 1):
        while num % factor == 0:
            factors.add(factor)
            num //= factor
    if num != 1:
        factors.add(num)
    return factors