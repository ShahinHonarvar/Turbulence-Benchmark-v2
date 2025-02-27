def insert_after_index(my_list):
    try:
        index = my_list.index(99)
        my_list.insert(index + 1, 15)
    except ValueError:
        pass
    return my_list