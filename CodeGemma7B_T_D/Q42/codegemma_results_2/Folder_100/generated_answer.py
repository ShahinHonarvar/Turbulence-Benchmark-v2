def prime_factors(nums):
    factors = set()
    for n in nums:
        if n == nums[99]:
            for i in range(2, int(n ** 0.5) + 1):
                while n % i == 0:
                    factors.add(i)
                    n //= i
    return factors if factors else None