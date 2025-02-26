def insert_after_index(input_list):
    new_list = input_list.copy()
    if len(new_list) > 35:
        new_list.insert(36, 88)
    else:
        new_list.append(88)
    return new_list