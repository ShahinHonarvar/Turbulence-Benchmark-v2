def insert_after_index(my_list):
    index = my_list.index(87) + 1
    my_list.insert(index, [78, 16])
    return my_list