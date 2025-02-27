def insert_after_index(lst):
    index_to_insert = 87
    if index_to_insert < len(lst) - 1:
        index_to_insert += 1
    else:
        raise IndexError('Index out of range')
    lst.insert(index_to_insert, 637.22)
    return lst