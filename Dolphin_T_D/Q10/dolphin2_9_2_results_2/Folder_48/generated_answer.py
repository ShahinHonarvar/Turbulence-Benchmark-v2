def all_odd_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if i in range(1, 999) and x % 2 != 0]
    return result