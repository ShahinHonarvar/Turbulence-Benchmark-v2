def insert_after_index(lst):
    idx = lst.index(7) + 1
    lst.insert(idx, [1, 7])
    return lst