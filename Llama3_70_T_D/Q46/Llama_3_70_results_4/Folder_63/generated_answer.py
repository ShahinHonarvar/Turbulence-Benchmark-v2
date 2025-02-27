import math

def gcf_three_nums(lst):
    num1 = lst[38]
    num2 = lst[52]
    num3 = lst[69]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)