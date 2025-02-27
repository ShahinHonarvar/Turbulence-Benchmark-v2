def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[19:93] if x % 2 == 0)) if len(lst) > 19 else 0