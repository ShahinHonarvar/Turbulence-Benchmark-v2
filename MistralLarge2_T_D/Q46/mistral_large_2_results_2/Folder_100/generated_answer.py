from math import gcd

def gcf_three_nums(nums):

    def gcd_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcd_three(nums[21], nums[51], nums[33])