from math import gcd

def gcf_two_nums(s):
    if len(s) < 723:
        return None
    return gcd(s[360], s[722])