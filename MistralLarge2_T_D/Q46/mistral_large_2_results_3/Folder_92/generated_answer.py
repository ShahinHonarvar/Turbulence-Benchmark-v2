from math import gcd

def gcf_three_nums(lst):
    num1 = lst[7]
    num2 = lst[9]
    num3 = lst[0]
    return gcd(gcd(num1, num2), num3)