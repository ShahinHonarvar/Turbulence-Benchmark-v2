def all_neg_ints_inclusive(lst):
    if not all((isinstance(i, int) for i in lst[80:201])):
        raise ValueError('All elements in the specified range must be integers')
    return [i for i in lst[80:201] if i < 0]