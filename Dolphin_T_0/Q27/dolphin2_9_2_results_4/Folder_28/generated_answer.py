def insert_after_index(lst):
    new_lst = lst[:]
    index_74 = new_lst.index(74)
    new_lst.insert(index_74 + 1, 49)
    return new_lst