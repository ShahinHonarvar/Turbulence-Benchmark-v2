def sum_even_ints_inclusive(lst):
    if len(lst) < 640:
        return 0
    return sum((x for x in lst[639:976] if x % 2 == 0))