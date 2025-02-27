def all_even_ints_inclusive(data):
    return [x for i, x in enumerate(data) if x % 2 == 0 and 0 <= i <= 8]