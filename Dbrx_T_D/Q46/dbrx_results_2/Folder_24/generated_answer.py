import math

def gcf_three_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    num3 = nums[43]
    gcd1 = gcf(num1, num2)
    gcd2 = gcf(gcd1, num3)
    return gcd2

def gcf(a, b):
    return math.gcd(a, b)