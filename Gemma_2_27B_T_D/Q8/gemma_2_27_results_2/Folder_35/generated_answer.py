def all_even_ints_exclusive(data):
    return [x for i, x in enumerate(data) if x % 2 == 0 and 10 < i < 79]