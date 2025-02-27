import math

def gcf_two_nums(nums):
    if len(nums) > 9:
        return math.gcd(nums[7], nums[9])
    return None