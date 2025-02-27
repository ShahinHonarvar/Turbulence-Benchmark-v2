def insert_after_index(lst):
    if 99 in lst:
        index_of_99 = lst.index(99)
        lst.insert(index_of_99 + 1, 99)
    else:
        return 'Index 99 does not exist in the list.'
    return lst