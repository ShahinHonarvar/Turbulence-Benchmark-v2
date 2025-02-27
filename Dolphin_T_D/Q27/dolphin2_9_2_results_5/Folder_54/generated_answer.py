def insert_after_index(lst):
    new_lst = lst[:]
    index = new_lst.index(43)
    new_lst.insert(index + 1, 37)
    return new_lst