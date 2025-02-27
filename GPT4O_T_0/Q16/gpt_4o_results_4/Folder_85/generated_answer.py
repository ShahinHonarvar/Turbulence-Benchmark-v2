def sum_even_ints_inclusive(lst):
    if len(lst) < 9:
        return 0
    return sum((x for x in lst[6:9] if x % 2 == 0))