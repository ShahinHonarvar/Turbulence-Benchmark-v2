def insert_after_index(lst):
    index = lst.index(2)
    new_lst = lst[:]
    new_lst.insert(index + 1, 8)
    return new_lst