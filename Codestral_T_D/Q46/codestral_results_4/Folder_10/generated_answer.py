import math

def gcf_three_nums(lst):
    num1 = lst[86]
    num2 = lst[89]
    num3 = lst[49]
    return math.gcd(math.gcd(num1, num2), num3)