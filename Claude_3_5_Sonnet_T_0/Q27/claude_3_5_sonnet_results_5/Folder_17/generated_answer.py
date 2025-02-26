def insert_after_index(lst):
    index = lst.index(94) if 94 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, 93)
    return new_list