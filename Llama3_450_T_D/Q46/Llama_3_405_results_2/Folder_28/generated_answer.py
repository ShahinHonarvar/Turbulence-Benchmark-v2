import math

def gcf_three_nums(nums):
    num1 = nums[99]
    num2 = nums[63]
    num3 = nums[74]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)