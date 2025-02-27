def insert_after_index(lst):
    new_lst = lst[:]
    new_lst.insert(lst.index(70) + 1, 76)
    return new_lst