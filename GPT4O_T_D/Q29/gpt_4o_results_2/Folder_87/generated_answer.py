from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 83:
        return gcd(nums[83], nums[14])
    return None