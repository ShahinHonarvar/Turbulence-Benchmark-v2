def insert_after_index(input_list):
    new_list = input_list.copy()
    if len(new_list) > 30:
        new_list.insert(31, 37)
    else:
        new_list.append(37)
    return new_list