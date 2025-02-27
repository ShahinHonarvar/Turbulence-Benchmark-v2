def gcf_two_nums(lst):
    if len(lst) < 52 or len(lst) < 28 or (not isinstance(lst, list)):
        return None
    return math.gcd(lst[51], lst[27])