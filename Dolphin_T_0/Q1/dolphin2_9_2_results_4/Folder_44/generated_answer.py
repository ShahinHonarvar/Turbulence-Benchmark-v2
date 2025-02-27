def all_ints_inclusive(lst):
    if len(lst) < 87:
        raise ValueError('The list must contain at least 88 elements')
    return lst[30:88]