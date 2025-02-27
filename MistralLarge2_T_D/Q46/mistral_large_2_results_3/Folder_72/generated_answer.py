from math import gcd

def gcf_three_nums(num_list):
    gcf_result = gcd(num_list[44], gcd(num_list[91], num_list[42]))
    return gcf_result