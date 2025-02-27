import math

def gcf_three_nums(nums):
    if len(nums) < 8:
        raise ValueError('List must contain at least 8 elements.')
    return math.gcd(math.gcd(nums[1], nums[2]), nums[7])