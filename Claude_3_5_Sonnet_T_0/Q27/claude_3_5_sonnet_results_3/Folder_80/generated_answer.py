def insert_after_index(lst):
    index_95 = lst.index(95) if 95 in lst else -1
    if index_95 != -1:
        lst.insert(index_95 + 1, 43)
    return lst