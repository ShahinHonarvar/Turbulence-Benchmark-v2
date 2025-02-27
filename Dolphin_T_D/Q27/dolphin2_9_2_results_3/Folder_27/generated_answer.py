def insert_after_index(lst):
    if 85 in lst:
        index = lst.index(85)
        lst.insert(index + 1, [41, 95])
    else:
        raise ValueError('Index 85 not found in the list')
    return lst