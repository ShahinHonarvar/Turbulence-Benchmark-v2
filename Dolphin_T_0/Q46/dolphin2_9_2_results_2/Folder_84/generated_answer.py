import math

def gcf_three_nums(lst):
    num1 = lst[695]
    num2 = lst[710]
    num3 = lst[914]
    return math.gcd(math.gcd(num1, num2), num3)