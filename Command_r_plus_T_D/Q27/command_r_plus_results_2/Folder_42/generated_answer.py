def insert_after_index(my_list):
    index = my_list.index(44) + 1
    my_list.insert(index, 40)
    my_list.insert(index + 1, 27)
    return my_list