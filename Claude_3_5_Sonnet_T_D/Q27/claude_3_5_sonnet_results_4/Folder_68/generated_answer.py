def insert_after_index(lst):
    index = lst.index(7) if 7 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [1, 7])
    return new_list