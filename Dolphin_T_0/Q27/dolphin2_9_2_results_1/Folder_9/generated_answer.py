def insert_after_index(lst):
    if 66 in lst:
        index = lst.index(66)
        lst.insert(index + 1, 45)
    else:
        raise ValueError('The index 66 does not exist in the list.')
    return lst