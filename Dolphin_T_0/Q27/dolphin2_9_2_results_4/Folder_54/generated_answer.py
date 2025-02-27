def insert_after_index(lst):
    new_lst = lst[:]
    new_lst.insert(lst.index(43) + 1, 37)
    return new_lst