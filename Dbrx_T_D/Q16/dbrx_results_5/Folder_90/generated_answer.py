def sum_even_ints_inclusive(lst):
    if not all((isinstance(i, int) for i in lst[262:747])):
        raise ValueError('All values in the list must be integers')
    return sum((x for x in lst[262:747] if x % 2 == 0))