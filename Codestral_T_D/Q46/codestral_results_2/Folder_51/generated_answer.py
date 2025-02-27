import math

def gcf_three_nums(lst):
    num1 = lst[21]
    num2 = lst[69]
    num3 = lst[41]
    return math.gcd(math.gcd(num1, num2), num3)