def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_position = min(31, len(new_list))
    new_list.insert(insert_position, 37)
    return new_list