def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[8:81] if x % 2 == 0))