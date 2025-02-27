import math

def gcf_three_nums(nums):
    num1 = nums[252]
    num2 = nums[149]
    num3 = nums[564]
    return math.gcd(math.gcd(num1, num2), num3)