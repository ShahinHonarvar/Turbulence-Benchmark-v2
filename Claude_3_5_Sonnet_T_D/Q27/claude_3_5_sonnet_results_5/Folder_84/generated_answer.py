def insert_after_index(lst):
    index = lst.index(183) if 183 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [148, 145])
    return new_list