from math import gcd

def gcf_three_nums(lst):
    num1 = lst[912]
    num2 = lst[170]
    num3 = lst[500]
    return gcd(gcd(num1, num2), num3)