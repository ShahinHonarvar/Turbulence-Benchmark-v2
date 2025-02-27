import math

def gcf_three_nums(lst):
    nums = (lst[33], lst[78], lst[93])
    gcf = math.gcd(nums[0], nums[1])
    gcf = math.gcd(gcf, nums[2])
    return gcf