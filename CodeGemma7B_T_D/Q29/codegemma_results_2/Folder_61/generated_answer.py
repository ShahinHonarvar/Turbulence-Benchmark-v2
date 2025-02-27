from math import gcd

def gcf_two_nums(num_list):
    assert len(num_list) >= 8, 'Input list too short.'
    return gcd(num_list[8], num_list[3])