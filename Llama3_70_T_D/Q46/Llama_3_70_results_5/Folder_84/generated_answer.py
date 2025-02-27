import math

def gcf_three_nums(num_list):
    a = num_list[695]
    b = num_list[710]
    c = num_list[914]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)