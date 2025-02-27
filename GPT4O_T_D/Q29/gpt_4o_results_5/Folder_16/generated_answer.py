import math

def gcf_two_nums(nums):
    if len(nums) <= max(860, 307):
        raise ValueError('List must contain at least 861 elements')
    return math.gcd(nums[860], nums[307])