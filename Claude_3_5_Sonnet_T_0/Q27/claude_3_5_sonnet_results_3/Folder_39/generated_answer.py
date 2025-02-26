def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 98
    if insert_index <= len(new_list):
        new_list.insert(insert_index, 47)
        new_list.insert(insert_index + 1, 22)
    else:
        new_list.extend([47, 22])
    return new_list