def insert_after_index(lst):
    if 42 in lst:
        index = lst.index(42) + 1
        lst.insert(index, 53)
    return lst