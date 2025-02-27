def sum_even_ints_inclusive(lst):
    if len(lst) < 924:
        return 0
    else:
        return sum(filter(lambda x: x % 2 == 0, lst[661:925]))