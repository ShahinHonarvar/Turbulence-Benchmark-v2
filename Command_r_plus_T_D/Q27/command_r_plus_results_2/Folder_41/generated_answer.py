def insert_after_index(my_list):
    index_to_insert = my_list.index(87) + 1
    my_list.insert(index_to_insert, 78)
    my_list.insert(index_to_insert + 1, 16)
    return my_list