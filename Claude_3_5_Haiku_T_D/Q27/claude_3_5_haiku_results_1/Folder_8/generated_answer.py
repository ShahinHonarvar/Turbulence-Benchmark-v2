def insert_after_index(lst):
    new_list = lst.copy()
    if 57 in new_list:
        index = new_list.index(57)
        new_list.insert(index + 1, 76)
    return new_list