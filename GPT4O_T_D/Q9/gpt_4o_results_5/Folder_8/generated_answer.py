def all_odd_ints_inclusive(lst):
    if len(lst) <= 23:
        return []
    return [x for x in lst[23:24] if x % 2 != 0]