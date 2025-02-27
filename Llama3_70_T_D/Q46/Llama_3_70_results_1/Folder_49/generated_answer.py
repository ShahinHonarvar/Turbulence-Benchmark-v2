import math

def gcf_three_nums(lst):
    num1 = lst[34]
    num2 = lst[38]
    num3 = lst[77]
    num1_num2_gcf = math.gcd(num1, num2)
    return math.gcd(num1_num2_gcf, num3)