from math import gcd

def apply_gcd(a, b):
    return gcd(a, b)

def gcf_three_nums(nums):
    nums = [nums[558], nums[110], nums[628]]
    result = reduce(apply_gcd, nums)
    return result