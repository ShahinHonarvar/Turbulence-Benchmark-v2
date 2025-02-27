from math import gcd

def gcf_three_nums(lst):
    num1 = lst[990]
    num2 = lst[671]
    num3 = lst[711]
    return gcd(gcd(num1, num2), num3)