def insert_after_index(lst):
    index = lst.index(52) if 52 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, 38)
    return new_list