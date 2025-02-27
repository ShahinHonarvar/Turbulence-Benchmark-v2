def all_odd_ints_inclusive(lst):
    if len(lst) < 93:
        return []
    return [x for x in lst[19:93] if x % 2 != 0]