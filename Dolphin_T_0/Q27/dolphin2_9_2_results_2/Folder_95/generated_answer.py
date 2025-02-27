def insert_after_index(lst):
    new_list = lst[:]
    new_list.insert(lst.index(20) + 1, 80)
    return new_list