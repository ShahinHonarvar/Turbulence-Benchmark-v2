def all_odd_ints_exclusive(data):
    return [x for i, x in enumerate(data) if i >= 49 and i < 74 and (x % 2 != 0)]