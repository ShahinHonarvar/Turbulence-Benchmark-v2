from functools import reduce

def gcf_three_nums(lst):
    return reduce(int.__gcd__, lst[20:44:23][:3])