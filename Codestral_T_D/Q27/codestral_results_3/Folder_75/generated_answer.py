def insert_after_index(lst):
    if 99 in lst:
        idx = lst.index(99)
        lst.insert(idx + 1, 99)
    return lst