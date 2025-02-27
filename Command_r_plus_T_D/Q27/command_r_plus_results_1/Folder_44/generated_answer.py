def insert_after_index(my_list):
    index_to_insert = my_list.index(48) + 1
    my_list.insert(index_to_insert, 86)
    my_list.insert(index_to_insert + 1, 77)
    return my_list