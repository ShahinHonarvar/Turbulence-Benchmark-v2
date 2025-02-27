def all_odd_ints_inclusive(lst):
    if not any((x % 2 for x in lst)):
        return []
    return lst[42:52:2]