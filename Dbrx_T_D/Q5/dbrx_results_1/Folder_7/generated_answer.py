def all_neg_ints_inclusive(lst):
    if not all((isinstance(i, int) for i in lst)):
        raise ValueError('All elements in the list must be integers')
    return [i for i in lst[660:925] if i < 0]