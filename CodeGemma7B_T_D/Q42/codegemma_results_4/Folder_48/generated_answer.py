def prime_factors(nums):
    return {factor for factor in factors_set(nums[247])}

def factors_set(num):
    return set((factor for factor in range(2, num) if num % factor == 0))