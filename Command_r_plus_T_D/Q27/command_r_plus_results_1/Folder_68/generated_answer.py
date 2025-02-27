def insert_after_index(my_list):
    index_7 = my_list.index(7)
    my_list.insert(index_7 + 1, [1, 7])
    return my_list