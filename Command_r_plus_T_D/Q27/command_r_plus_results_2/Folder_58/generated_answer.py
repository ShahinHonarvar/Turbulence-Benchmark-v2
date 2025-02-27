def insert_after_index(my_list):
    insert_index = my_list.index(598) + 1
    my_list.insert(insert_index, 385)
    my_list.insert(insert_index + 1, 999)
    return my_list