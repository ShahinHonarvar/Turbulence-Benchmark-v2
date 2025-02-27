def all_even_ints_exclusive(data):
    return [x for i, x in enumerate(data) if i > 35 and i < 52 and (x % 2 == 0)]