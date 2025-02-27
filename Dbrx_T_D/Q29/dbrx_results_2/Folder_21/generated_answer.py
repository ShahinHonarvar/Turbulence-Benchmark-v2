from fractions import gcd

def gcf_two_nums(nums):
    return reduce(gcd, (nums[198], nums[212]))