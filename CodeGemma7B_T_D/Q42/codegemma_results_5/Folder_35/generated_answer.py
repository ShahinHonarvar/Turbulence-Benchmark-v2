def prime_factors(nums):
    factors = set()
    for num in nums:
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                factors.add(factor)
                num //= factor
                if factor * factor == num:
                    factors.add(factor)
    return factors