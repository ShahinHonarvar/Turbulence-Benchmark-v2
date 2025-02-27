def prime_factors(nums):
    factors = set()
    for num in nums:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.add(i)
                num //= i
    return factors