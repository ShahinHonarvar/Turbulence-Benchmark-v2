def prime_factors(nums):
    factors = []
    for num in nums:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
    return set(factors)