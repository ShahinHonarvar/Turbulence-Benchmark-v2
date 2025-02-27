def insert_after_index(lst):
    new_lst = lst.copy()
    index = new_lst.index(99)
    new_lst.insert(index + 1, 99)
    return new_lst