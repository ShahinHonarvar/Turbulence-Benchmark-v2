def insert_after_index(lst):
    copy_lst = lst.copy()
    copy_lst.insert(lst.index(166) + 1, 232)
    return copy_lst