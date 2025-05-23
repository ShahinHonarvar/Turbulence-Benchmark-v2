import math

def gcf_three_nums(nums):
    num1 = nums[76]
    num2 = nums[64]
    num3 = nums[28]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)