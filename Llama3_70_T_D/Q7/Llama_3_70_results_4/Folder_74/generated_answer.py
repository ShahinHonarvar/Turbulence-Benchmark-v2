def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[17:79], start=17) if x % 2 == 0]