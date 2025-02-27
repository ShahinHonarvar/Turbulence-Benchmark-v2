import math

def gcf_three_nums(lst):
    num1 = lst[66]
    num2 = lst[56]
    num3 = lst[92]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)