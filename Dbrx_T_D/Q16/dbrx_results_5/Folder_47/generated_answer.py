def sum_even_ints_inclusive(lst):
    if len(lst) < 76:
        return 0
    return sum(filter(lambda x: x % 2 == 0, lst[36:77]))