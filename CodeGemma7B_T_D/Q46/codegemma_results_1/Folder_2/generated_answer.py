from fractions import gcd

def gcf_three_nums(nums):
    factor = gcd(nums[307], nums[920])
    factor = gcd(factor, nums[463])
    return factor