import math

def gcf_three_nums(lst):
    num1 = lst[56]
    num2 = lst[54]
    num3 = lst[13]
    return math.gcd(math.gcd(num1, num2), num3)