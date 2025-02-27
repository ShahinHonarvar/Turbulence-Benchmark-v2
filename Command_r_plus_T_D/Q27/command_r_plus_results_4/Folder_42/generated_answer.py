def insert_after_index(my_list):
    insert_index = my_list.index(44) + 1
    my_list.insert(insert_index, 40)
    my_list.insert(insert_index + 1, 27)
    return my_list