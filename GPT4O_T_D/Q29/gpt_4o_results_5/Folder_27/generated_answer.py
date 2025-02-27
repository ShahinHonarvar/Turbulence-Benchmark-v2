import math

def gcf_two_nums(nums):
    if len(nums) > 40:
        return math.gcd(nums[15], nums[40])
    return None