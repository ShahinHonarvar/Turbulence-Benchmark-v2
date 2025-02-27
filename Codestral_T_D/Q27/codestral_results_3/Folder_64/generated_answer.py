def insert_after_index(lst):
    if 8 in lst:
        index = lst.index(8)
        lst.insert(index + 1, [3, 8])
    return lst