import math

def gcf_three_nums(nums):
    if len(nums) < 52:
        raise ValueError('List must contain at least 52 elements')
    return math.gcd(math.gcd(nums[21], nums[51]), nums[33])