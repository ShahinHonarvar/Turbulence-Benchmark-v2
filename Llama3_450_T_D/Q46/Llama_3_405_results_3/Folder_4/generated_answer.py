import math

def gcf_three_nums(num_list):
    num1 = num_list[24]
    num2 = num_list[25]
    num3 = num_list[80]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)