from math import gcd

def gcf_two_nums(nums):
    if len(nums) < 70:
        return None
    return gcd(nums[41], nums[69])