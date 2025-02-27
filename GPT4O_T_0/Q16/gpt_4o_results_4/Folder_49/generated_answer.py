def sum_even_ints_inclusive(lst):
    if len(lst) < 9:
        return 0
    return sum((x for x in lst[8:81] if x % 2 == 0))