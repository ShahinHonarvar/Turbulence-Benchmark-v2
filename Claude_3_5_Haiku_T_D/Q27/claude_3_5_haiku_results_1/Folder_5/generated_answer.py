def insert_after_index(input_list):
    if len(input_list) > 99:
        input_list.insert(100, 15)
    return input_list