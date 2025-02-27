def insert_after_index(my_list):
    index_to_insert = my_list.index(598) + 1
    my_list.insert(index_to_insert, 385)
    my_list.insert(index_to_insert + 1, 999)
    return my_list