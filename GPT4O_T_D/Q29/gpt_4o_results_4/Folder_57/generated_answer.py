from math import gcd

def gcf_two_nums(nums):
    if len(nums) <= 49:
        return None
    return gcd(nums[28], nums[49])