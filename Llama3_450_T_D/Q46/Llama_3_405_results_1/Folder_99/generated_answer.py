import math

def gcf_three_nums(nums):
    num1 = nums[912]
    num2 = nums[170]
    num3 = nums[500]
    return math.gcd(math.gcd(num1, num2), num3)