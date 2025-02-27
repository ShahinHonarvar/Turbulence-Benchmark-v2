def all_even_ints_exclusive(lst):
    return [n for i, n in enumerate(lst) if 42 < i < 87 and n % 2 == 0]