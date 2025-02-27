def prime_factors(nums):
    prime_factors = set()
    for num in nums:
        if num > 1:
            for divisor in range(2, int(num ** 0.5) + 1):
                while num % divisor == 0:
                    num //= divisor
                    prime_factors.add(divisor)
    return prime_factors