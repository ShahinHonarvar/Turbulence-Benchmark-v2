def insert_after_index(lst):
    copy_lst = lst.copy()
    copy_lst.insert(lst.index(21) + 1, 74)
    return copy_lst