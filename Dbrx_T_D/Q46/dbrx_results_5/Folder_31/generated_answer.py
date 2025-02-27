import math

def gcf_three_nums(nums):
    num1 = nums[90]
    num2 = nums[54]
    num3 = nums[96]
    factor1 = math.gcd(num1, num2)
    factor2 = math.gcd(factor1, num3)
    return factor2