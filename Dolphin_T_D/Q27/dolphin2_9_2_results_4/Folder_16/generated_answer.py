def insert_after_index(lst):
    new_lst = lst[:]
    index = lst.index(983)
    new_lst.insert(index + 1, 369)
    return new_lst