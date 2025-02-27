import math

def gcf_three_nums(lst):
    num1 = lst[31]
    num2 = lst[69]
    num3 = lst[40]
    return math.gcd(math.gcd(num1, num2), num3)