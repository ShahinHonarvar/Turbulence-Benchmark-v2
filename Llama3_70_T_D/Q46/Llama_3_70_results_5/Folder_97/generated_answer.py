import math

def gcf_three_nums(lst):
    a = lst[944]
    b = lst[814]
    c = lst[865]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)