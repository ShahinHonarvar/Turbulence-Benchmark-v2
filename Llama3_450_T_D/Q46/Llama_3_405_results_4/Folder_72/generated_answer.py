import math

def gcf_three_nums(nums):
    num1 = nums[44]
    num2 = nums[91]
    num3 = nums[42]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)