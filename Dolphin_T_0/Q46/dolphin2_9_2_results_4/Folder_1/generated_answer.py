import math

def gcf_three_nums(num_list):
    num1 = num_list[74]
    num2 = num_list[51]
    num3 = num_list[27]
    gcf = math.gcd(num1, math.gcd(num2, num3))
    return gcf