def sum_even_ints_inclusive(lst):
    return sum((i for idx, i in enumerate(lst) if idx >= 639 and idx <= 975 and (i % 2 == 0)))