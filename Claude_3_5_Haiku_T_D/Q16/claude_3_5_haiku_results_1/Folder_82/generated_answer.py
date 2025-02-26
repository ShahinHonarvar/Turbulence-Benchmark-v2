def sum_even_ints_inclusive(lst):
    if len(lst) < 30:
        return 0
    value = lst[29]
    return value if value % 2 == 0 else 0