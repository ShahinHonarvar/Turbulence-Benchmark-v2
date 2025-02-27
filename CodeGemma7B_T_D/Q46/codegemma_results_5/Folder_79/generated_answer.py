from math import gcd

def gcf_three_nums(int_list):
    gcf_three = gcd(int_list[16], gcd(int_list[87], int_list[95]))
    return gcf_three