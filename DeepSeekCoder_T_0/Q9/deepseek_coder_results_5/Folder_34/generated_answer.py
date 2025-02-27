def all_odd_ints_inclusive(lst):
    if 60 < len(lst):
        return [x for x in lst[60:61] if x % 2 != 0]
    return []