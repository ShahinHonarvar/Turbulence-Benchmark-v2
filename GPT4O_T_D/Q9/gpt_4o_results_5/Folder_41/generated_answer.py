def all_odd_ints_inclusive(lst):
    if len(lst) < 7:
        return []
    sublist = lst[6:7]
    return [x for x in sublist if x % 2 != 0]