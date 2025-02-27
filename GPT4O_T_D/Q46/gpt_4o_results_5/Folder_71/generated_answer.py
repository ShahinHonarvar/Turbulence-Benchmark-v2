import math

def gcf_three_nums(nums):
    if len(nums) < 46:
        return None
    return math.gcd(math.gcd(nums[24], nums[45]), nums[38])