import math

def gcf_three_nums(lst):
    num1 = lst[93]
    num2 = lst[94]
    num3 = lst[57]
    return math.gcd(num1, math.gcd(num2, num3))