import math

def gcf_three_nums(nums):
    num1 = nums[85]
    num2 = nums[36]
    num3 = nums[54]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)