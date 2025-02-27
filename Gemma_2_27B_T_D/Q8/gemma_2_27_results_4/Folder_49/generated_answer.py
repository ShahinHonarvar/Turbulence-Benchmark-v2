def all_even_ints_exclusive(data):
    return [x for i, x in enumerate(data) if i >= 80 and i < 200 and (x % 2 == 0)]