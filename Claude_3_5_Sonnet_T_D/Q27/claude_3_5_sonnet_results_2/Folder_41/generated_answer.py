def insert_after_index(lst):
    index = lst.index(87) if 87 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [78, 16])
    return new_list