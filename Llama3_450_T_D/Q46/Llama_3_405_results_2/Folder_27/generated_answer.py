import math

def gcf_three_nums(num_list):
    num1 = num_list[76]
    num2 = num_list[64]
    num3 = num_list[28]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf