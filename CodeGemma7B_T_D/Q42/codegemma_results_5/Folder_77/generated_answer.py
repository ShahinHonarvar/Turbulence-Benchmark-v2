def prime_factors(nums):
    num = nums[985]
    prime_factors_set = set()
    for factor in range(2, int(num ** 0.5) + 1):
        while num % factor == 0:
            prime_factors_set.add(factor)
            num //= factor
    if num > 1:
        prime_factors_set.add(num)
    return prime_factors_set