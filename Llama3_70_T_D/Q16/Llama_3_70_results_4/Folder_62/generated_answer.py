def sum_even_ints_inclusive(lst):
    if len(lst) < 100:
        return 0
    return sum((i for i in lst[91:100] if i % 2 == 0))