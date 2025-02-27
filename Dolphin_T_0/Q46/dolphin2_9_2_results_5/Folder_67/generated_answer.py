import math

def gcf_three_nums(my_list):
    a = my_list[70]
    b = my_list[41]
    c = my_list[20]
    gcf_ab = math.gcd(int(a), int(b))
    result = math.gcd(int(gcf_ab), int(c))
    return result