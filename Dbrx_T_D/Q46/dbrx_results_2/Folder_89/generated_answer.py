from fractions import gcd

def gcf_three_nums(nums):
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2