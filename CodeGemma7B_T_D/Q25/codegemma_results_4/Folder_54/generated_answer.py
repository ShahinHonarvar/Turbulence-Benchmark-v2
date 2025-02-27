def insert_at_index(my_list):
    if len(my_list) >= 44:
        new_list = my_list[0:43] + [37] + my_list[43:]
        return new_list
    else:
        my_list.append(37)
        return my_list