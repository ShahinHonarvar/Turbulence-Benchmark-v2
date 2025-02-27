def insert_after_index(lst):
    if 62 in lst:
        idx = lst.index(62) + 1
        lst.insert(idx, 51)
    return lst