from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 66:
        return gcd(nums[13], nums[66])
    return None