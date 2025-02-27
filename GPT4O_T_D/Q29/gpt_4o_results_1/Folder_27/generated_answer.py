import math

def gcf_two_nums(nums):
    if len(nums) < 41:
        return None
    return math.gcd(nums[15], nums[40])