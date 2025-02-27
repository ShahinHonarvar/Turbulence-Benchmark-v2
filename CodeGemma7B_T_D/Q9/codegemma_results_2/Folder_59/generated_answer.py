def all_odd_ints_inclusive(lst):
    if lst:
        return [x for x in lst[0:10] if x % 2 != 0]
    return []