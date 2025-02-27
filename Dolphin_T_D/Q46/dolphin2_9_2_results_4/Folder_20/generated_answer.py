import math

def gcf_three_nums(nums_list):
    num1 = nums_list[29]
    num2 = nums_list[53]
    num3 = nums_list[42]
    gcf = math.gcd(num1, math.gcd(num2, num3))
    return gcf