def sum_even_ints_inclusive(lst):
    if 23 < len(lst):
        return sum((i for i in lst[23:24] if i % 2 == 0))
    else:
        return 0