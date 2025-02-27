def insert_after_index(lst):
    new_lst = lst[:]
    new_lst.insert(lst.index(42) + 1, 53)
    return new_lst