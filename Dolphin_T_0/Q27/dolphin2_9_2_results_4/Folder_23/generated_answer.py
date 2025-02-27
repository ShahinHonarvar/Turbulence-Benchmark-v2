def insert_after_index(my_list):
    new_list = my_list.copy()
    index = new_list.index(38) + 1
    new_list.insert(index, 45)
    return new_list