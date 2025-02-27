def all_odd_ints_inclusive(lst):
    if not lst or lst[0] % 2 == 0 or lst[-1] % 2 == 0:
        return []
    return lst[::2]