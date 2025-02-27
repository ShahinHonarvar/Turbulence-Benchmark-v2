from math import gcd

def gcf_three_nums(nums):

    def gcd_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcd_three(nums[49], nums[46], nums[13])