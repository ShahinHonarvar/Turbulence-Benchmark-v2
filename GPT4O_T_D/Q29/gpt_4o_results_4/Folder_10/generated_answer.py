import math

def gcf_two_nums(nums):
    if len(nums) > 99:
        return math.gcd(nums[15], nums[99])
    return None