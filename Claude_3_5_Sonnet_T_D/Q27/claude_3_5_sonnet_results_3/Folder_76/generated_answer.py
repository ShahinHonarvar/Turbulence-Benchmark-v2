def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 167
    if insert_index <= len(new_list):
        new_list.insert(insert_index, 232)
    return new_list