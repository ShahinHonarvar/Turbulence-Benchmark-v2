from math import gcd

def gcf_three_nums(nums):
    if len(nums) > 77:
        gcf = gcd(nums[34], gcd(nums[38], nums[77]))
        return gcf
    else:
        return None