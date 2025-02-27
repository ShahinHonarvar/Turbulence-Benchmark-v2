def all_even_ints_exclusive(data):
    return [x for i, x in enumerate(data) if i >= 70 and i < 98 and (x % 2 == 0)]