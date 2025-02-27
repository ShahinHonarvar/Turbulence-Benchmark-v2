import math

def gcf_three_nums(nums):
    num1 = nums[93]
    num2 = nums[94]
    num3 = nums[57]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)