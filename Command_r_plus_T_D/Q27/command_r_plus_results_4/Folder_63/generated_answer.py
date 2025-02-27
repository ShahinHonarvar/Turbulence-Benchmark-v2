def insert_after_index(my_list):
    index = my_list.index(76) + 1
    my_list.insert(index, 15)
    my_list.insert(index + 1, 51)
    return my_list