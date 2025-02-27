import math

def gcf_two_nums(nums):
    if len(nums) > max(56, 88):
        return math.gcd(nums[56], nums[88])
    return None