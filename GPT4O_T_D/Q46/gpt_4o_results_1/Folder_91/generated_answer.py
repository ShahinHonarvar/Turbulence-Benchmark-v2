import math

def gcf_three_nums(num_list):
    if len(num_list) < 10:
        raise ValueError('List must contain at least 10 elements.')
    a, b, c = (num_list[8], num_list[9], num_list[3])
    return math.gcd(math.gcd(a, b), c)