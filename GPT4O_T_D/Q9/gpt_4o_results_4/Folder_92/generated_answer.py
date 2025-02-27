def all_odd_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    return [x for x in lst[:2] if x % 2 != 0]