def insert_after_index(lst):
    new_lst = lst[:]
    new_lst.insert(lst.index(761) + 1, 925)
    return new_lst