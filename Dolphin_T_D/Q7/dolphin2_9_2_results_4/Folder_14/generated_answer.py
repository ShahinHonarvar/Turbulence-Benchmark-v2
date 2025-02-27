def all_even_ints_inclusive(l):
    return [x for i, x in enumerate(l) if 5 <= i <= 7 and x % 2 == 0]