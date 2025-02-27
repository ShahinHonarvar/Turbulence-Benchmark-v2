import math

def gcf_three_nums(lst):
    a = lst[990]
    b = lst[671]
    c = lst[711]
    return math.gcd(math.gcd(a, b), c)