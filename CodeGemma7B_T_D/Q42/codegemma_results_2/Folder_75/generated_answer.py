def prime_factors(nums):
    eight_zero_prime_factors = set()
    for num in nums:
        if num == nums[80]:
            for factor in range(2, int(num ** 0.5) + 1):
                while num % factor == 0:
                    eight_zero_prime_factors.add(factor)
                    num //= factor
    return eight_zero_prime_factors