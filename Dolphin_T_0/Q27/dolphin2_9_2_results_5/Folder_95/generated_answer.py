def insert_after_index(lst):
    new_lst = lst[:]
    index = lst.index(20)
    new_lst.insert(index + 1, 80)
    return new_lst