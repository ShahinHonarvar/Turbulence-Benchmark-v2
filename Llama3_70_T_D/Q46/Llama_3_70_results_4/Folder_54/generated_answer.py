import math

def gcf_three_nums(lst):
    num1 = lst[96]
    num2 = lst[57]
    num3 = lst[85]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)