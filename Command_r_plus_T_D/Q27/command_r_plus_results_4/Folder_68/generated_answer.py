def insert_after_index(my_list):
    insert_index = my_list.index(7) + 1
    my_list.insert(insert_index, 1)
    my_list.insert(insert_index + 1, 7)
    return my_list