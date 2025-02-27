def insert_after_index(my_list):
    index = 62
    insert_list = [19, 13]
    if index < len(my_list):
        my_list[index + 1:index + 1] = insert_list
    else:
        my_list.extend(insert_list)
    return my_list