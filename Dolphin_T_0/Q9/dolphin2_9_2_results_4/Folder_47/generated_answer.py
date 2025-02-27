def all_odd_ints_inclusive(lst):
    result = [n for i, n in enumerate(lst[37:77]) if n % 2 != 0]
    return result