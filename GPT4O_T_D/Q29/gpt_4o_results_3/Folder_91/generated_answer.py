from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 4:
        return gcd(nums[0], nums[4])
    return None