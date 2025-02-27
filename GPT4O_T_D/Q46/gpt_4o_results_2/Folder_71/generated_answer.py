import math

def gcf_three_nums(nums):
    if len(nums) <= max(24, 45, 38):
        raise ValueError('List must contain at least 46 elements.')
    return math.gcd(math.gcd(nums[24], nums[45]), nums[38])