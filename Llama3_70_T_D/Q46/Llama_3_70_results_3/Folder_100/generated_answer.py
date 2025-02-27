import math

def gcf_three_nums(num_list):
    num1 = num_list[21]
    num2 = num_list[51]
    num3 = num_list[33]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)