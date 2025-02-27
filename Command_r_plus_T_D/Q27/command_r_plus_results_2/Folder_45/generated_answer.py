def insert_after_index(my_list):
    index = my_list.index(84) + 1
    my_list.insert(index, 13)
    my_list.insert(index + 1, 46)
    return my_list