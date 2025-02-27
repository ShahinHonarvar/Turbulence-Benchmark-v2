import math

def gcf_three_nums(lst):
    num1 = lst[53]
    num2 = lst[23]
    num3 = lst[45]
    return math.gcd(math.gcd(num1, num2), num3)