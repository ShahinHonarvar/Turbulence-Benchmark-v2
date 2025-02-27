def all_odd_ints_inclusive(lst):
    if 23 < len(lst):
        return [x for x in lst[23:24] if x % 2 != 0]
    return []