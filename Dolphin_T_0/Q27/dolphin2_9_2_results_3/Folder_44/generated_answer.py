def insert_after_index(lst):
    new_lst = lst[:]
    index = new_lst.index(48)
    new_lst.insert(index + 1, [86, 77])
    return new_lst