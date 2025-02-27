def all_ints_inclusive(lst):
    if len(lst) < 85:
        raise IndexError('List not long enough to have index 84')
    return lst[70:85]