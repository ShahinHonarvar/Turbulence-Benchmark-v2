import math

def gcf_three_nums(nums):
    num1 = nums[96]
    num2 = nums[57]
    num3 = nums[85]
    factors1 = [factor for factor in range(1, num1 + 1) if num1 % factor == 0]
    factors2 = [factor for factor in range(1, num2 + 1) if num2 % factor == 0]
    factors3 = [factor for factor in range(1, num3 + 1) if num3 % factor == 0]
    common_factors = [factor for factor in factors1 if factor in factors2 and factor in factors3]
    return max(common_factors)