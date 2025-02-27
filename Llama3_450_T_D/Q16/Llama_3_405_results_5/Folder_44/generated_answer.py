def sum_even_ints_inclusive(lst):
    return sum((i for idx, i in enumerate(lst) if 13 <= idx <= 68 and i % 2 == 0))