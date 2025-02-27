def sum_even_ints_inclusive(lst):
    if len(lst) < 16:
        return 0
    return sum((x for x in lst[15:40] if x % 2 == 0))