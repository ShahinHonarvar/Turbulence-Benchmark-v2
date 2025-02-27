import math

def gcf_three_nums(num_list):
    num1 = num_list[991]
    num2 = num_list[244]
    num3 = num_list[974]
    gcf_12 = math.gcd(num1, num2)
    gcf = math.gcd(gcf_12, num3)
    return gcf