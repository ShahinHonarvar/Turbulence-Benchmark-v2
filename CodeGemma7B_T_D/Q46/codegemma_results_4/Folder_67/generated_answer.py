from math import gcd

def gcf_three_nums(int_list):
    num1, num2, num3 = (int_list[70], int_list[41], int_list[20])
    return gcd(num1, gcd(num2, num3))