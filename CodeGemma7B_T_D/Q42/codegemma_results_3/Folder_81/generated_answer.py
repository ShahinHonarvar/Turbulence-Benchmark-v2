def prime_factors(nums):
    factors = set()
    for num in nums:
        for i in range(2, num + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
    return factors