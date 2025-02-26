def insert_after_index(lst):
    index = lst.index(983) if 983 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, 369)
    return new_list