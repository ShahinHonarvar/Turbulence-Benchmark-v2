import math

def gcf_three_nums(nums):
    num1 = nums[36]
    num2 = nums[85]
    num3 = nums[83]
    gcf_12 = math.gcd(num1, num2)
    gcf = math.gcd(gcf_12, num3)
    return gcf