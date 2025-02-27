import math

def gcf_three_nums(l):
    a = math.gcd(l[14], l[21])
    b = math.gcd(a, l[17])
    return b