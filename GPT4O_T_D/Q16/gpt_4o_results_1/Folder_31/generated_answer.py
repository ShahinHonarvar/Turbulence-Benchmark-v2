def sum_even_ints_inclusive(lst):
    if len(lst) < 89:
        return 0
    return sum((i for i in lst[75:89] if i % 2 == 0))