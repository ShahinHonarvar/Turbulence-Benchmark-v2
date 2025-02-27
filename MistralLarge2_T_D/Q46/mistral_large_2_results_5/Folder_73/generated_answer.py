import math

def gcf_three_nums(lst):
    num1 = lst[90]
    num2 = lst[84]
    num3 = lst[47]
    return math.gcd(math.gcd(num1, num2), num3)