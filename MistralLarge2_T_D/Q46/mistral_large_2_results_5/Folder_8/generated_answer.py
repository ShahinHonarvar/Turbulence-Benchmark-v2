from math import gcd

def gcf_three_nums(lst):
    num1, num2, num3 = (lst[99], lst[28], lst[53])
    return gcd(gcd(num1, num2), num3)