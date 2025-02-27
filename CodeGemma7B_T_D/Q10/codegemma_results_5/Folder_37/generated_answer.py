def all_odd_ints_exclusive(lst):
    ss = [e for i, e in enumerate(lst) if i > 0 and i < 2 and (e % 2 != 0)]
    return ss