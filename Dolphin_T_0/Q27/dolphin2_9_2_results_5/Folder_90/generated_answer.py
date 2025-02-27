def insert_after_index(lst):
    new_lst = lst.copy()
    index = new_lst.index(761) + 1
    new_lst.insert(index, 925)
    return new_lst