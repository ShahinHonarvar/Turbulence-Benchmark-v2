def insert_after_index(lst):
    if 96 in lst:
        index = lst.index(96) + 1
        lst.insert(index, 36)
    return lst