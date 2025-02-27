def insert_after_index(lst):
    if 99 in lst:
        lst.insert(lst.index(99) + 1, 15)
    return lst