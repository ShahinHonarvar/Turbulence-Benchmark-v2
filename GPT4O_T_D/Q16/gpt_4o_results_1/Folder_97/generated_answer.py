def sum_even_ints_inclusive(lst):
    if len(lst) < 41:
        return 0
    return sum((i for i in lst[40:81] if i % 2 == 0))