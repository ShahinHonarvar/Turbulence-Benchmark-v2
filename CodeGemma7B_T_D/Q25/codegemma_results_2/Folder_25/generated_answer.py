def insert_at_index(my_list):
    new_list = my_list
    if len(new_list) < 31:
        new_list.append(None)
    new_list[30] = 37
    return new_list