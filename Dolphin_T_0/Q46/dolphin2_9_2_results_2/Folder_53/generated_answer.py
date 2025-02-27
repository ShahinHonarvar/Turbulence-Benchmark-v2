import math

def gcf_three_nums(list_nums):
    num1 = list_nums[66]
    num2 = list_nums[56]
    num3 = list_nums[92]
    gcd_nums = math.gcd(num1, num2)
    result = math.gcd(gcd_nums, num3)
    return result