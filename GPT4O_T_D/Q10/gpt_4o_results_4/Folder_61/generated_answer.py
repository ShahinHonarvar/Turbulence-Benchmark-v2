def all_odd_ints_exclusive(lst):
    if len(lst) <= 2:
        return []
    return [x for x in lst[1:7] if x % 2 != 0]