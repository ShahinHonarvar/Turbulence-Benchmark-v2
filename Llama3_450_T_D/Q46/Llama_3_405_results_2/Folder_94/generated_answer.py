import math

def gcf_three_nums(num_list):
    num1 = num_list[56]
    num2 = num_list[88]
    num3 = num_list[51]
    gcf_12 = math.gcd(num1, num2)
    gcf = math.gcd(gcf_12, num3)
    return gcf