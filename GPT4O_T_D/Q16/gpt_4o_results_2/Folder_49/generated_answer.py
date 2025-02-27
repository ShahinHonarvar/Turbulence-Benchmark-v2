def sum_even_ints_inclusive(lst):
    if len(lst) < 9:
        return 0
    return sum((i for i in lst[8:81] if i % 2 == 0))