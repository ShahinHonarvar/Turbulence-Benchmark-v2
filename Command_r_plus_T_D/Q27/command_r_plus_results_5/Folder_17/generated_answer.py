def insert_after_index(my_list):
    try:
        index = my_list.index(94)
        my_list.insert(index + 1, 93)
        return my_list
    except ValueError:
        return my_list