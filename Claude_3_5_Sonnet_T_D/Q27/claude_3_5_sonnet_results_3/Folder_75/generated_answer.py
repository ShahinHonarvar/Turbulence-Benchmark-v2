def insert_after_index(lst):
    new_list = lst.copy()
    if 99 in new_list:
        index = new_list.index(99)
        new_list.insert(index + 1, 99)
    return new_list