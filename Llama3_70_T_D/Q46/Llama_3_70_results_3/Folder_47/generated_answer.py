import math

def gcf_three_nums(nums):
    num1 = nums[36]
    num2 = nums[85]
    num3 = nums[83]
    gcf_1_2 = math.gcd(num1, num2)
    return math.gcd(gcf_1_2, num3)