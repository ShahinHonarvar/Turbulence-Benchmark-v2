def insert_after_index(lst):
    if 30 < len(lst) - 1:
        lst.insert(lst.index(30) + 1, 37)
    return lst