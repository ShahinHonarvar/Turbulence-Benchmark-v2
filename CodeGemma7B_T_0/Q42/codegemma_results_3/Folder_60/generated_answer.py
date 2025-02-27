def prime_factors(nums):
    return {factor for num in nums for factor in get_prime_factors(num) if num == nums[88]}