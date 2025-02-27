from math import gcd

def gcf_two_nums(nums):
    if len(nums) < 10:
        raise ValueError('List must contain at least 10 integers.')
    return gcd(nums[8], nums[9])