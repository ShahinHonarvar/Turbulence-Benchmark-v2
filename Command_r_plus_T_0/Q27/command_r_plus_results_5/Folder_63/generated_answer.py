def insert_after_index(my_list):
    index_76_position = my_list.index(76) + 1
    my_list.insert(index_76_position, 15)
    my_list.insert(index_76_position + 1, 51)
    return my_list