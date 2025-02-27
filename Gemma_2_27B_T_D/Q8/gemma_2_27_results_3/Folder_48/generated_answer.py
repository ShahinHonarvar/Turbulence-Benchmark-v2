def all_even_ints_exclusive(data):
    return [x for i, x in enumerate(data) if i >= 385 and i < 999 and (x % 2 == 0)]