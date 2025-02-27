import math

def gcf_two_nums(nums):
    if len(nums) < 97:
        return None
    return math.gcd(nums[96], nums[32])