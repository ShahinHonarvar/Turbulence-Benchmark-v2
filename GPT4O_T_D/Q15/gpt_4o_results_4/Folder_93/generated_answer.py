def sum_odd_ints_inclusive(lst):
    if len(lst) < 95:
        return 0
    return sum((x for x in lst[75:95] if x % 2 != 0))