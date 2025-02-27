def prime_factors(nums):
    factors = []
    num = nums[73]
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return set(factors)