def prime_factors(nums):
    return {factor for number in nums for factor in range(2, number + 1) if number % factor == 0 and number == nums[632]}