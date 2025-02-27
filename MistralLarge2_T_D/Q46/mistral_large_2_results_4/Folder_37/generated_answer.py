from math import gcd

def gcf_three_nums(lst):
    num1 = lst[41]
    num2 = lst[69]
    num3 = lst[28]
    return gcd(gcd(num1, num2), num3)