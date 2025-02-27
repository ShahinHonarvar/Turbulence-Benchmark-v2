def sum_even_ints_inclusive(lst):
    if len(lst) < 6:
        return 0
    return sum((x for x in lst[3:6] if x % 2 == 0))