import math

def gcf_three_nums(lst):
    num1 = lst[90]
    num2 = lst[54]
    num3 = lst[96]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf