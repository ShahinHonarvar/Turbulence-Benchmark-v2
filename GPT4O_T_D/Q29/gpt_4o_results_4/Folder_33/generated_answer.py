import math

def gcf_two_nums(nums):
    if len(nums) <= 166 or len(nums) <= 106:
        return None
    return math.gcd(nums[166], nums[106])