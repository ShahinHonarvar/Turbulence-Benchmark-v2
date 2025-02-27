import math

def gcf_two_nums(nums):
    if len(nums) <= max(25, 80):
        return None
    return math.gcd(nums[25], nums[80])