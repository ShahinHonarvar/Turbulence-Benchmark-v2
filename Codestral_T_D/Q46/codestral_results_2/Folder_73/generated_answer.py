import math

def gcf_three_nums(num_list):
    num1 = num_list[90]
    num2 = num_list[84]
    num3 = num_list[47]
    gcf = math.gcd(num1, num2)
    gcf = math.gcd(gcf, num3)
    return gcf