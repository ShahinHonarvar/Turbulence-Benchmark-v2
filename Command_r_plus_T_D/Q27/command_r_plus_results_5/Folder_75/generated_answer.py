def insert_after_index(my_list):
    index = my_list.index(99)
    my_list.insert(index + 1, 99)
    return my_list