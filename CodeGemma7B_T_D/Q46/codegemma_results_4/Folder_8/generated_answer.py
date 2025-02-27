from math import gcd

def gcf_three_nums(num_list):
    first = gcd(num_list[99], num_list[28])
    return gcd(first, num_list[53])