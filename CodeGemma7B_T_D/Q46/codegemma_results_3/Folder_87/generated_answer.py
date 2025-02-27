from math import gcd

def gcf_three_nums(nums):
    num1 = nums[74]
    num2 = nums[60]
    num3 = nums[28]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf