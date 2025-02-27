from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 85:
        return gcd(gcd(lst[27], lst[85]), lst[51])
    return None