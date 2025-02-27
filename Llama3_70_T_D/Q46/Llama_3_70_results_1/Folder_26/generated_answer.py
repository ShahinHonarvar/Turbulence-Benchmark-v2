import math

def gcf_three_nums(lst):
    num1 = lst[15]
    num2 = lst[51]
    num3 = lst[76]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)