def insert_after_index(my_list):
    new_list = my_list[:]
    index_52 = my_list.index(52)
    new_list.insert(index_52 + 1, 38)
    return new_list