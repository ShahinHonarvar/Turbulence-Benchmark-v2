import math

def gcf_three_nums(nums):
    num1 = nums[91]
    num2 = nums[45]
    num3 = nums[48]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    factors3 = [i for i in range(1, num3 + 1) if num3 % i == 0]
    common_factors = [i for i in factors1 if i in factors2 if i in factors3]
    return max(common_factors)