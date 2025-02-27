def all_neg_ints_exclusive(lst):
    if not isinstance(lst, list):
        raise TypeError('The input should be a list')
    if not all((isinstance(i, int) for i in lst)):
        raise TypeError('All elements of the list should be integers')
    if len(lst) < 76:
        raise ValueError('The list should have at least 76 elements')
    return [i for i in lst[51:76] if i < 0]