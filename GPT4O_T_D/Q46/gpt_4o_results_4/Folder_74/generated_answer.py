import math

def gcf_three_nums(lst):
    if len(lst) < 100:
        return None
    num1 = lst[99]
    num2 = lst[95]
    num3 = lst[80]
    return math.gcd(math.gcd(num1, num2), num3)