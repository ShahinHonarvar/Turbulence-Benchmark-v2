def insert_after_index(lst):
    new_lst = lst[:]
    index = new_lst.index(606) + 1
    new_lst.insert(index, [606, 873])
    return new_lst