def insert_after_index(lst):
    new_lst = lst.copy()
    index = new_lst.index(412) + 1
    new_lst.insert(index, 668)
    return new_lst