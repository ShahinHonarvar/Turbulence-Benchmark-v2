import math

def gcf_three_nums(num_list):
    gcf = math.gcd(math.gcd(num_list[33], num_list[78]), num_list[93])
    return gcf