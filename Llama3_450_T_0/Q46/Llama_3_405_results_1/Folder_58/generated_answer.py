import math

def gcf_three_nums(nums):
    num1 = nums[145]
    num2 = nums[183]
    num3 = nums[770]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)