from math import gcd       

def gcf_two_nums(nums):
    if len(nums) != 532:
        raise ValueError('The list should have 532 elements')
    return gcd(nums[180], nums[312])