def insert_after_index(lst):
    index = lst.index(43) if 43 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, 37)
    return new_list