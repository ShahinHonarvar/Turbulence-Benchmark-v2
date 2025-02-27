import math

def gcf_three_nums(num_list):
    num1 = num_list[99]
    num2 = num_list[28]
    num3 = num_list[53]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf