def sum_even_ints_inclusive(lst):
    if len(lst) - 1 < 20 or len(lst) - 1 < 30:
        return 0
    else:
        sublist = lst[20:31]
        return sum((i for i in sublist if i % 2 == 0))