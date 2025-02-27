import math

def gcf_two_nums(nums):
    if len(nums) > 27:
        return math.gcd(nums[23], nums[27])
    return None