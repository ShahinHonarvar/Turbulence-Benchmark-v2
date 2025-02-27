def insert_after_index(input_list):
    if len(input_list) > 100:
        input_list.insert(101, 876)
        input_list.insert(102, 203)
    else:
        input_list.insert(100, 876)
        input_list.insert(101, 203)
    return input_list