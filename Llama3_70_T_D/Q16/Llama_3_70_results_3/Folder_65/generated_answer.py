def sum_even_ints_inclusive(lst):
    if len(lst) <= 98:
        return sum((i for i in lst[56:] if i % 2 == 0))
    else:
        return sum((i for i in lst[56:99] if i % 2 == 0))