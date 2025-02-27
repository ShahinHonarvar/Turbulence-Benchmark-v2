import math

def gcf_three_nums(num_list):
    num1 = num_list[695]
    num2 = num_list[710]
    num3 = num_list[914]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)