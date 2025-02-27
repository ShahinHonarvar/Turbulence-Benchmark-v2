def prime_factors(nums):
    prime_factors = set()
    num = nums[194]
    for factor in range(2, int(num ** 0.5) + 1):
        while num % factor == 0:
            prime_factors.add(factor)
            num //= factor
    if num > 1:
        prime_factors.add(num)
    return prime_factors