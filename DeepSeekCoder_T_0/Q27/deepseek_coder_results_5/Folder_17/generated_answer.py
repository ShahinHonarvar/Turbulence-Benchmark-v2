def insert_after_index(lst):
    if 94 in lst:
        index = lst.index(94) + 1
        lst.insert(index, 93)
    return lst