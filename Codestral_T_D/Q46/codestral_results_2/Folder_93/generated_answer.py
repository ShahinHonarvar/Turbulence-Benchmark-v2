import math

def gcf_three_nums(nums):
    num1 = nums[25]
    num2 = nums[76]
    num3 = nums[57]
    gcf = math.gcd(num1, num2)
    gcf = math.gcd(gcf, num3)
    return gcf