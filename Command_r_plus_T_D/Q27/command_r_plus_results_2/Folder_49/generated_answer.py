def insert_after_index(my_list):
    insert_index = my_list.index(38) + 1
    my_list.insert(insert_index, 27)
    my_list.insert(insert_index + 1, 34)
    return my_list