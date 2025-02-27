import math

def gcf_three_nums(nums):
    if len(nums) < 10:
        raise ValueError('Input list must be of length at least 10')
    return math.gcd(math.gcd(nums[7], nums[9]), nums[0])