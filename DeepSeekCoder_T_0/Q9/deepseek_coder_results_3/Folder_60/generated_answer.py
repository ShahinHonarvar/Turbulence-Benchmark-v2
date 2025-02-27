def all_odd_ints_inclusive(lst):
    return [x for x in lst[75:86] if x % 2 != 0] if len(lst) > 85 else []