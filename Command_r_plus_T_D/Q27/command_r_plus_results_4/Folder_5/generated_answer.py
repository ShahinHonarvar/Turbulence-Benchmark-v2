def insert_after_index(my_list):
    try:
        index_99 = my_list.index(99)
        my_list.insert(index_99 + 1, 15)
    except ValueError:
        pass
    return my_list