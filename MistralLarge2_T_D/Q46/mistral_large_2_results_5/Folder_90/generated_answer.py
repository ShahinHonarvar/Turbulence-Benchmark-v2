from math import gcd

def gcf_three_nums(lst):
    num1 = lst[818]
    num2 = lst[606]
    num3 = lst[873]
    return gcd(gcd(num1, num2), num3)