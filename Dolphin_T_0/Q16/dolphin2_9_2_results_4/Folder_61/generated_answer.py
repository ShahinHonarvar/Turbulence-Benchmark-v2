def sum_even_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst) if i < 8 and val % 2 == 0))