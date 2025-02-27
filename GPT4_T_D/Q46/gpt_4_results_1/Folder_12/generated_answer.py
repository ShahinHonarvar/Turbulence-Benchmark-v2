from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 92:
        return 'List is too short'
    else:
        return gcd(gcd(lst[91], lst[45]), lst[48])