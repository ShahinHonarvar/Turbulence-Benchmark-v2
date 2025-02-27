import math

def gcf_three_nums(num_list):
    num1 = num_list[49]
    num2 = num_list[46]
    num3 = num_list[13]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)