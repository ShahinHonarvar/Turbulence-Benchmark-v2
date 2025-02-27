from math import gcd

def gcf_three_nums(numbers_list):
    gcf = gcd(numbers_list[25], numbers_list[76])
    gcf = gcd(gcf, numbers_list[57])
    return gcf