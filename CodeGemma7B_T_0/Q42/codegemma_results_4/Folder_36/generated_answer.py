def prime_factors(nums):
    return {factor for factor in range(2, nums[990] + 1) if nums[990] % factor == 0}