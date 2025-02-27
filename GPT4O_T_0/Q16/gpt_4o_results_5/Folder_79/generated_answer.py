def sum_even_ints_inclusive(lst):
    if len(lst) < 5:
        return 0
    return lst[4] if lst[4] % 2 == 0 else 0