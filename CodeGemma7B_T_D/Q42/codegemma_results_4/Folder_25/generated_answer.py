def prime_factors(nums):
    return prime_factors_helper(nums, 90)

def prime_factors_helper(nums, idx):
    if idx < 0 or idx >= len(nums):
        raise IndexError('Invalid index')
    num = nums[idx]