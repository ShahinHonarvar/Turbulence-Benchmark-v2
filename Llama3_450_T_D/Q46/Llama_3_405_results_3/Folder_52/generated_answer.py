import math

def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]
    gcf1_2 = math.gcd(num1, num2)
    return math.gcd(gcf1_2, num3)