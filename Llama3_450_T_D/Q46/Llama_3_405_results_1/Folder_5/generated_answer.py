import math

def gcf_three_nums(nums):
    num1 = nums[64]
    num2 = nums[80]
    num3 = nums[15]
    gcf12 = math.gcd(num1, num2)
    gcf = math.gcd(gcf12, num3)
    return gcf