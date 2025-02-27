from math import gcd

def gcf_three_nums(num_list):
    return gcd(num_list[99], gcd(num_list[95], num_list[80]))