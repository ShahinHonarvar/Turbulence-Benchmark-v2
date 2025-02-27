def insert_after_index(my_list):
    new_list = my_list.copy()
    index_to_insert = my_list.index(66) + 1
    new_list.insert(index_to_insert, 45)
    return new_list