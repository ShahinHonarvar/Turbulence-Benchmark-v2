import math

def gcf_three_nums(nums):
    num1 = nums[86]
    num2 = nums[89]
    num3 = nums[49]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)