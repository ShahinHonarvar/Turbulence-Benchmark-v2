def insert_at_index(my_list):
    if len(my_list) >= 500:
        my_list.insert(500, [912, 170])
    else:
        my_list.append([912, 170])
    return my_list