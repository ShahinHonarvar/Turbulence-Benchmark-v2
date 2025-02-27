from math import gcd

def gcf_two_nums(num_list):
    if len(num_list) > 9:
        return gcd(num_list[6], num_list[9])
    return None