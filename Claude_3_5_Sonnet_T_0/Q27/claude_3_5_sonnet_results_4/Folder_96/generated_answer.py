def insert_after_index(lst):
    index = lst.index(74) if 74 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [51, 29])
    return new_list