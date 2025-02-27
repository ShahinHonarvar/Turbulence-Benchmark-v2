def sum_even_ints_inclusive(lst):
    if len(lst) < 85:
        return 0
    return sum((i for i in lst[70:85] if i % 2 == 0))