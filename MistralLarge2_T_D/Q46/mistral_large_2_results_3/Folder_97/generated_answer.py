from math import gcd

def gcf_three_nums(nums):
    num1 = nums[944]
    num2 = nums[814]
    num3 = nums[865]
    return gcd(gcd(num1, num2), num3)