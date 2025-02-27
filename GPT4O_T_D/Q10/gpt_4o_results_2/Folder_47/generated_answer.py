def all_odd_ints_exclusive(lst):
    if len(lst) <= 65:
        return []
    return [x for x in lst[65:80] if x % 2 != 0]