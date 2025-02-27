def sum_even_ints_inclusive(lst):
    if len(lst) < 7 or lst[6] % 2 != 0:
        return 0
    return lst[6]