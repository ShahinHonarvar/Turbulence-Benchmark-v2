def all_odd_ints_inclusive(lst):
    if len(lst) < 11:
        return []
    return [x for x in lst[10:11] if x % 2 != 0]