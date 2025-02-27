def sum_even_ints_inclusive(lst):
    return sum((i for idx, i in enumerate(lst) if 90 <= idx <= 200 and i % 2 == 0))