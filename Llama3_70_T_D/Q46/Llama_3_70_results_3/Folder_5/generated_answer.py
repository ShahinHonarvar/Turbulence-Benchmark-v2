import math

def gcf_three_nums(lst):
    num1 = lst[64]
    num2 = lst[80]
    num3 = lst[15]
    gcf_1_2 = math.gcd(num1, num2)
    return math.gcd(gcf_1_2, num3)