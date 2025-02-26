def insert_after_index(input_list):
    if 87 in input_list:
        insert_pos = input_list.index(87) + 1
        input_list.insert(insert_pos, 78)
        input_list.insert(insert_pos + 1, 16)
    return input_list