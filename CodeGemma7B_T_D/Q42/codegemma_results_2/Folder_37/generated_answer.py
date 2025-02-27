def prime_factors(nums):
    return {i for i in nums[28] if all((i % j != 0 for j in range(2, i)))}