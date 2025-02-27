import math

def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[25]
    num2 = list_of_nums[80]
    gcd = math.gcd(num1, num2)
    factors_of_gcd = [factor for factor in range(1, gcd + 1) if gcd % factor == 0]
    greatest_common_factor = max(factors_of_gcd)
    return greatest_common_factor