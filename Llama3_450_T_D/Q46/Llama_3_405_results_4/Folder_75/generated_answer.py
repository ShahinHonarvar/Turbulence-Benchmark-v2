import math

def gcf_three_nums(nums):
    num1 = nums[70]
    num2 = nums[98]
    num3 = nums[22]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)