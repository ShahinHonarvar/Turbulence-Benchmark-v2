def insert_after_index(lst):
    index = lst.index(85) if 85 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [41, 95])
    return new_list