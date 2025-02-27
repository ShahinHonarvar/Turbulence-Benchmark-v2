def sum_even_ints_inclusive(lst):
    if len(lst) < 99:
        return 0
    return sum((i for i in lst[55:99] if i % 2 == 0))