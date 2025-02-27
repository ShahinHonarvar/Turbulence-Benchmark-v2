def insert_after_index(lst):
    new_lst = lst[:]
    index_57 = new_lst.index(57)
    new_lst.insert(index_57 + 1, 76)
    return new_lst