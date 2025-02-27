import math

def gcf_two_nums(nums):
    if len(nums) < 97:
        raise ValueError('List must contain at least 97 elements')
    return math.gcd(nums[96], nums[57])