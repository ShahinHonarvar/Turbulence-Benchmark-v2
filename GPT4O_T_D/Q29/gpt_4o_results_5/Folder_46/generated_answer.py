import math

def gcf_two_nums(nums):
    if len(nums) < 55:
        return None
    return math.gcd(nums[36], nums[54])