import math

def gcf_three_nums(lst):
    num1 = lst[34]
    num2 = lst[38]
    num3 = lst[77]
    return math.gcd(math.gcd(num1, num2), num3)