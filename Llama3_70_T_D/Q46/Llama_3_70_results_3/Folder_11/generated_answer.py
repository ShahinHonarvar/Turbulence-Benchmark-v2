import math

def gcf_three_nums(lst):
    num1 = lst[37]
    num2 = lst[30]
    num3 = lst[48]
    return math.gcd(math.gcd(num1, num2), num3)