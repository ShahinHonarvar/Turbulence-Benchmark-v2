def prime_factors(nums):
    prime_factors = set()
    for num in nums:
        if num == nums[733]:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    prime_factors.add(factor)
    return prime_factors