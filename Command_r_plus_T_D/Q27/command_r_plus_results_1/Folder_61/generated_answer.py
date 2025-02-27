def insert_after_index(my_list):
    new_list = my_list.copy()
    new_list.insert(new_list.index(4) + 1, 7)
    return new_list