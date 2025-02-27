import math

def gcf_three_nums(num_list):
    num1 = num_list[654]
    num2 = num_list[312]
    num3 = num_list[441]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)