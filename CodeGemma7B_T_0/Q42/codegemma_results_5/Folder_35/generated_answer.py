def prime_factors(nums):
    return {factor for factor in set(prime_factorize(nums[993])) if factor in nums}