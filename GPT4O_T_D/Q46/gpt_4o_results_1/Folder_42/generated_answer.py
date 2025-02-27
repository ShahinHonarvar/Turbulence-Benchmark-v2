import math

def gcf_three_nums(num_list):
    if len(num_list) > 97:
        return math.gcd(math.gcd(num_list[19], num_list[69]), num_list[97])
    else:
        return None