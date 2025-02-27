import math

def gcf_three_nums(nums):
    num1, num2 = (nums[56], nums[92])
    num3 = nums[66]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [j for j in range(1, num2 + 1) if num2 % j == 0]
    factors3 = [k for k in range(1, num3 + 1) if num3 % k == 0]
    common_factors = set(factors1 + factors2 + factors3)
    gcf = max(common_factors)
    return gcf