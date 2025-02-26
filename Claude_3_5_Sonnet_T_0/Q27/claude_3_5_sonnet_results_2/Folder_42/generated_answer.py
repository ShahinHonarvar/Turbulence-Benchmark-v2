def insert_after_index(lst):
    index = lst.index(44) if 44 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [40, 27])
    return new_list