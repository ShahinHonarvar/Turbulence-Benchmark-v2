def all_odd_ints_exclusive(lst):
    if len(lst) <= 50:
        return []
    return [x for x in lst[50:74] if x % 2 != 0]