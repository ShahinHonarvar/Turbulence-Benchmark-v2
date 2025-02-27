def all_odd_ints_inclusive(lst):
    if len(lst) <= 60:
        return []
    return [x for x in lst[60:61] if x % 2 != 0]