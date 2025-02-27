import math

def gcf_two_nums(nums):
    if len(nums) < 48:
        return None
    return math.gcd(nums[47], nums[22])