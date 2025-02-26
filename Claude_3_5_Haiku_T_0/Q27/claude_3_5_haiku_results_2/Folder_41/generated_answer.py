def insert_after_index(input_list):
    if 87 in input_list:
        index = input_list.index(87)
        input_list.insert(index + 1, 78)
        input_list.insert(index + 2, 16)
    return input_list