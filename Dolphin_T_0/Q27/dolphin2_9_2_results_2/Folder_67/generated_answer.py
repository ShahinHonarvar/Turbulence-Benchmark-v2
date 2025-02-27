def insert_after_index(lst):
    new_lst = lst[:]
    index = new_lst.index(44)
    new_lst.insert(index + 1, 76)
    return new_lst