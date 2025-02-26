def insert_after_index(lst):
    index = lst.index(62) if 62 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, 51)
    return new_list