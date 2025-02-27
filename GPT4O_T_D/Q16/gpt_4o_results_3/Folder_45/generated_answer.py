def sum_even_ints_inclusive(lst):
    if len(lst) < 31:
        return 0
    return sum((x for x in lst[30:min(201, len(lst))] if x % 2 == 0))