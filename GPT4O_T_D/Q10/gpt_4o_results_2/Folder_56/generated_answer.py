def all_odd_ints_exclusive(lst):
    if len(lst) < 10:
        return []
    return [x for x in lst[8:9] if x % 2 != 0]