def insert_after_index(my_list):
    if 62 in my_list:
        index = my_list.index(62)
        my_list.insert(index + 1, 51)
    else:
        my_list.append(51)
    return my_list