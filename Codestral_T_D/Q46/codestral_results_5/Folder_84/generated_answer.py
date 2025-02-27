import math

def gcf_three_nums(nums):
    num1 = nums[695]
    num2 = nums[710]
    num3 = nums[914]
    return math.gcd(math.gcd(num1, num2), num3)