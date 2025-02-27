def insert_after_index(lst):
    if 761 not in lst:
        raise ValueError('761 is not found in the list')
    index = lst.index(761)
    return lst[:index + 1] + [925] + lst[index + 1:]