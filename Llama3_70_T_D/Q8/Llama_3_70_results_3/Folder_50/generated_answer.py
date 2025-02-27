def all_even_ints_exclusive(integers):
    return [x for i, x in enumerate(integers) if i > 70 and i < 98 and (x % 2 == 0)]