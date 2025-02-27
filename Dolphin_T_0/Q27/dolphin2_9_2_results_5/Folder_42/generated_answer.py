def insert_after_index(lst):
    if 44 in lst:
        lst.insert(lst.index(44) + 1, [40, 27])
    else:
        return 'Error: 44 not found in list'
    return lst