def insert_after_index(my_list):
    try:
        index = my_list.index(94)
        my_list.insert(index + 1, 93)
    except ValueError:
        pass
    return my_list