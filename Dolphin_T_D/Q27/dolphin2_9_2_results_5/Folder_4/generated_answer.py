def insert_after_index(lst):
    new_lst = lst[:]
    new_lst.insert(lst.index(60) + 1, [80, 74])
    return new_lst