from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[944], lst[814], lst[865])
    return gcd(gcd(a, b), c)