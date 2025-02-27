import math

def gcf_three_nums(nums):
    num1 = nums[742]
    num2 = nums[888]
    num3 = nums[629]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf