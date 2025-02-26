def insert_after_index(lst):
    index = lst.index(55) if 55 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [26, 10])
    return new_list