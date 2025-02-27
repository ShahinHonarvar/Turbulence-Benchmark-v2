from math import gcd

def gcf_three_nums(numbers):
    a, _, b, c, *_ = numbers
    return gcd(a, gcd(b, c))