def insert_after_index(lst):
    lst = lst.copy()
    index = lst.index(56)
    lst.insert(index + 1, 54)
    return lst