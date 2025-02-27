def all_odd_ints_exclusive(lst):
    if len(lst) > 2:
        return [x for x in lst[1:-1] if x % 2 != 0]
    return []