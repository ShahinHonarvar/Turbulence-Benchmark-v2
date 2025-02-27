import math

def gcf_three_nums(num_list):
    num1 = num_list[742]
    num2 = num_list[888]
    num3 = num_list[629]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf