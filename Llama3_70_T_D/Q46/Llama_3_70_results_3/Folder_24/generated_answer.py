import math

def gcf_three_nums(lst):
    num1 = lst[18]
    num2 = lst[37]
    num3 = lst[43]
    gcf_12 = math.gcd(num1, num2)
    gcf = math.gcd(gcf_12, num3)
    return gcf