def prime_factors(nums):
    return {n for i, num in enumerate(nums) for n in range(2, int(num ** 0.5) + 1) if num % n == 0 and i == 222}