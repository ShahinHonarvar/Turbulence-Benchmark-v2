import math

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return abs(a)

def gcf_three_nums(nums):
    num1 = nums[90]
    num2 = nums[41]
    num3 = nums[95]
    return int(math.sqrt(gcd(num1, gcd(num2, num3)) ** 2))