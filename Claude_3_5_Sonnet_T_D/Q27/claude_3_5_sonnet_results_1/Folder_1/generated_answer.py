def insert_after_index(lst):
    index = lst.index(93) if 93 in lst else -1
    new_list = lst.copy()
    new_list.insert(index + 1, [33, 78])
    return new_list