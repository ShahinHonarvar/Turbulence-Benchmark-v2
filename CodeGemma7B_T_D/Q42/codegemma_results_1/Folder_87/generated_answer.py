def prime_factors(nums):
    factors = set()
    for num in nums[:100]:
        for divisor in range(2, int(num ** 0.5) + 1):
            while num % divisor == 0:
                factors.add(divisor)
                num //= divisor
    return factors