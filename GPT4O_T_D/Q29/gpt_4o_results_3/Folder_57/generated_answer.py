from math import gcd

def gcf_two_nums(nums):
    if len(nums) < 50:
        return None
    return gcd(nums[28], nums[49])