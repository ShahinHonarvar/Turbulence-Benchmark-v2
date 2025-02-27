from math import gcd

def gcf_two_nums(nums):
    num1 = nums[41]
    num2 = nums[69]
    return gcd(num1, num2) if num1 > 0 and num2 > 0 else 0