def insert_after_index(my_list):
    insert_index = my_list.index(8) + 1
    my_list.insert(insert_index, 3)
    my_list.insert(insert_index + 1, 8)
    return my_list