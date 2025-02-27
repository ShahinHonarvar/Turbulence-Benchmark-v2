def insert_after_index(lst):
    index = lst.index(97)
    new_lst = lst[:]
    new_lst.insert(index + 1, 72.27)
    return new_lst