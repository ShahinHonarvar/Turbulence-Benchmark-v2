def insert_after_index(my_list):
    insert_index = my_list.index(60) + 1
    my_list.insert(insert_index, 80)
    my_list.insert(insert_index + 1, 74)
    return my_list