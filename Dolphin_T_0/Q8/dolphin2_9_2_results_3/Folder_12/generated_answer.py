def all_even_ints_exclusive(l):
    return [x for i, x in enumerate(l[24:45]) if i % 2 == 0 and x % 2 == 0]