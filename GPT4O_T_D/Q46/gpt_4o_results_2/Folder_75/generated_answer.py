import math

def gcf_three_nums(lst):
    if len(lst) < 99:
        return None
    num1 = lst[70]
    num2 = lst[98]
    num3 = lst[22]
    return math.gcd(math.gcd(num1, num2), num3)