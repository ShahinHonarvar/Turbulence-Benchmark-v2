def insert_after_index(lst):
    new_list = lst[:]
    new_list.insert(lst.index(166) + 1, 232)
    return new_list