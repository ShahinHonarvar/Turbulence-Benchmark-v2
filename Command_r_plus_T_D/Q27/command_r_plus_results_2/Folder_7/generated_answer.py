def insert_after_index(input_list):
    insert_index = input_list.index(323) + 1
    input_list.insert(insert_index, 389)
    input_list.insert(insert_index + 1, 303)
    return input_list