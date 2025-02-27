def insert_after_index(lst):
    if 32 in lst:
        index = lst.index(32) + 1
        lst.insert(index, [54, 96])
    return lst