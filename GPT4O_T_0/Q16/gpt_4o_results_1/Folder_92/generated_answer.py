def sum_even_ints_inclusive(lst):
    if len(lst) < 2:
        return 0
    return sum((x for x in lst[0:2] if x % 2 == 0))