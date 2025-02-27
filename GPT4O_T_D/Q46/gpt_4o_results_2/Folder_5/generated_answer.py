import math

def gcf_three_nums(num_list):
    if len(num_list) > max(64, 80, 15):
        return math.gcd(math.gcd(num_list[64], num_list[80]), num_list[15])
    return None