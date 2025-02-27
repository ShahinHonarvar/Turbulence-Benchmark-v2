def sum_even_ints_inclusive(lst):
    return sum((i for i in lst[36:47] if i % 2 == 0)) if len(lst) > 46 else 0