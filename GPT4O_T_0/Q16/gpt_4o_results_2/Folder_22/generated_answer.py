def sum_even_ints_inclusive(lst):
    if len(lst) < 42:
        return 0
    return sum((x for x in lst[40:42] if x % 2 == 0))