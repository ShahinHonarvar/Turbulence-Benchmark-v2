def insert_after_index(lst):
    copy_lst = lst.copy()
    index = copy_lst.index(166)
    copy_lst.insert(index + 1, 232)
    return copy_lst