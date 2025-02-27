def prime_factors(nums):
    prime_set = set()
    num = nums[845]
    for factor in range(2, num + 1):
        while num % factor == 0:
            prime_set.add(factor)
            num //= factor
    return prime_set