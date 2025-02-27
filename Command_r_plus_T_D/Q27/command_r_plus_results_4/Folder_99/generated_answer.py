def insert_after_index(my_list):
    index_to_insert = my_list.index(295) + 1
    my_list.insert(index_to_insert, 276)
    my_list.insert(index_to_insert + 1, 376)
    return my_list