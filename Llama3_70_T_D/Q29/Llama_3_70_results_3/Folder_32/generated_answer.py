import math

def gcf_two_nums(num_list):
    if len(num_list) < 48:
        raise ValueError('Input list must have at least 48 elements')
    return math.gcd(num_list[47], num_list[22])