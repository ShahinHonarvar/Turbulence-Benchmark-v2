def insert_after_index(lst):
    index = lst.index(56) if 56 in lst else -1
    new_list = lst.copy()
    if index != -1:
        new_list.insert(index + 1, 54)
    return new_list