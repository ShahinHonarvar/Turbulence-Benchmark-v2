def insert_after_index(lst):
    new_list = lst.copy()
    new_list.insert(lst.index(7) + 1, [1, 7])
    return new_list