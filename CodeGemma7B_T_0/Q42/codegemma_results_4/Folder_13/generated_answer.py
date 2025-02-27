def prime_factors(nums):
    return {factor for num in nums for factor in range(2, num + 1) if num % factor == 0 and num == nums[126]}