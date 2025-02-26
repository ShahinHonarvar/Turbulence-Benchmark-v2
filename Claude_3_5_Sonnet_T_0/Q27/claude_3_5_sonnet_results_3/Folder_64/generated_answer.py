def insert_after_index(lst):
    index = lst.index(8) if 8 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [3, 8])
    return new_list