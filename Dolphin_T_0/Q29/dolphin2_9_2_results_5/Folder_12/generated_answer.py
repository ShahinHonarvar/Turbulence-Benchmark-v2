def gcf_two_nums(lst):
    if len(lst) > 56 or len(lst) > 54:
        return math.gcd(lst[56], lst[54])
    else:
        return -1