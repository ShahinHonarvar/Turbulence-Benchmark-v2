import math

def gcf_three_nums(num_list):
    num1 = num_list[16]
    num2 = num_list[87]
    num3 = num_list[95]
    return math.gcd(math.gcd(num1, num2), num3)