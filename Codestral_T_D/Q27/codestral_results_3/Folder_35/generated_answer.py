def insert_after_index(lst):
    if 100 in lst:
        index = lst.index(100) + 1
        lst.insert(index, [876, 203])
    return lst