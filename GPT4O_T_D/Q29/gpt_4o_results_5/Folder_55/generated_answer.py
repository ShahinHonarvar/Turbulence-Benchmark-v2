from math import gcd

def gcf_two_nums(nums):
    if len(nums) < 3:
        return None
    return gcd(nums[2], nums[1])