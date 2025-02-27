import math

def gcf_three_nums(nums):
    num1 = nums[991]
    num2 = nums[244]
    num3 = nums[974]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)