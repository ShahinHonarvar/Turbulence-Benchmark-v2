def insert_after_index(my_list):
    index = my_list.index(183) + 1
    my_list.insert(index, 148)
    my_list.insert(index + 1, 145)
    return my_list