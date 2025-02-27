def insert_after_index(my_list):
    index_500_plus_1 = my_list.index(500) + 1
    my_list.insert(index_500_plus_1, 912)
    my_list.insert(index_500_plus_1 + 1, 170)
    return my_list