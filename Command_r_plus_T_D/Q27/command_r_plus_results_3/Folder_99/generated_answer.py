def insert_after_index(my_list):
    insert_index = my_list.index(295) + 1
    my_list.insert(insert_index, 276)
    my_list.insert(insert_index + 1, 376)
    return my_list