def insert_after_index(my_list):
    index_8 = my_list.index(8)
    my_list.insert(index_8 + 1, [3, 8])
    return my_list