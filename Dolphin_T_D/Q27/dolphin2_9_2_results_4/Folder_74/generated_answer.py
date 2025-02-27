def insert_after_index(lst):
    new_lst = lst.copy()
    new_lst.insert(new_lst.index(41) + 1, [74, 70])
    return new_lst