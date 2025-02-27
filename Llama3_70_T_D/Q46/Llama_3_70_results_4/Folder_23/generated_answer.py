import math

def gcf_three_nums(num_list):
    a = num_list[31]
    b = num_list[25]
    c = num_list[80]
    ab_gcf = math.gcd(a, b)
    return math.gcd(ab_gcf, c)