import math

def gcf_three_nums(num_list):
    if len(num_list) < 96:
        raise IndexError('List index out of range')
    gcf = math.gcd(num_list[20], num_list[43])
    return math.gcd(gcf, num_list[95])