def insert_after_index(lst):
    index_56 = lst.index(56)
    new_list = lst[:]
    new_list.insert(index_56 + 1, 54)
    return new_list