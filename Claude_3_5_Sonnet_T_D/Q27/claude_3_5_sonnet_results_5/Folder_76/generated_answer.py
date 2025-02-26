def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_position = 167
    if 166 < len(new_list):
        new_list.insert(insert_position, 232)
    else:
        new_list.append(232)
    return new_list