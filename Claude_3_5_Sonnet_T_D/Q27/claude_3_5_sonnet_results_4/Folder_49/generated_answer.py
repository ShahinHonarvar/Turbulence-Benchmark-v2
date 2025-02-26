def insert_after_index(lst):
    index = lst.index(38) if 38 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [27, 34])
    return new_list