def prime_factors(nums):
    return set([factor for num in nums if num == nums[247] for factor in range(2, int(num ** 0.5) + 1) if num % factor == 0])