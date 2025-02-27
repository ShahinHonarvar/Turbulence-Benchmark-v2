def sum_even_ints_inclusive(lst):
    return sum((i for idx, i in enumerate(lst) if 246 <= idx <= 750 and i % 2 == 0))