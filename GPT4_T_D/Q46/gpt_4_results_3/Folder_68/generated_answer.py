from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[1], num_list[4]), num_list[7])