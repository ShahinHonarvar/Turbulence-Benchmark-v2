def insert_after_index(lst):
    if 94 in lst:
        idx = lst.index(94) + 1
        lst.insert(idx, 93)
    return lst