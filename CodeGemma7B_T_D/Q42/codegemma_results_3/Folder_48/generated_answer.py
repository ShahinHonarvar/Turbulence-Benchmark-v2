def prime_factors(nums):
    prime_factors = set()
    for num in nums:
        for factor in range(2, num + 1):
            while num % factor == 0:
                prime_factors.add(factor)
                num //= factor
    return prime_factors