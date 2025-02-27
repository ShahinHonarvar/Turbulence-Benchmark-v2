import math

def gcf_three_nums(nums):
    num1 = nums[13]
    num2 = nums[76]
    num3 = nums[44]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)