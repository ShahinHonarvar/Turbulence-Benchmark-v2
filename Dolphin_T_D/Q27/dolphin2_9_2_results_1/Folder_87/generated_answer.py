def insert_after_index(lst):
    new_lst = lst[:]
    new_lst.insert(lst.index(69) + 1, 92)
    return new_lst