from math import gcd

def gcf_two_nums(num_list):
    if len(num_list) > 34:
        return gcd(num_list[27], num_list[34])