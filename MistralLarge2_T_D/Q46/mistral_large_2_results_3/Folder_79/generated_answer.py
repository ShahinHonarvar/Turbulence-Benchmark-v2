from math import gcd

def gcf_three_nums(lst):
    num1 = lst[16]
    num2 = lst[87]
    num3 = lst[95]
    return gcd(gcd(num1, num2), num3)