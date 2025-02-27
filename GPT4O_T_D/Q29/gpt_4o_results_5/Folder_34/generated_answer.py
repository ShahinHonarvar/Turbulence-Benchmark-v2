import math

def gcf_two_nums(nums):
    if len(nums) > 64:
        return math.gcd(nums[60], nums[64])
    return None