from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 8:
        return gcd(nums[8], nums[3])
    return None