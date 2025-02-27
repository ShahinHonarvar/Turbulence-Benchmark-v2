def insert_after_index(lst):
    index = lst.index(42) if 42 in lst else len(lst)
    new_lst = lst[:]
    new_lst.insert(index + 1, 53)
    return new_lst