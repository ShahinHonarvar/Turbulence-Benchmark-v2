def insert_after_index(lst):
    new_lst = lst.copy()
    index = lst.index(56)
    new_lst.insert(index + 1, 54)
    return new_lst