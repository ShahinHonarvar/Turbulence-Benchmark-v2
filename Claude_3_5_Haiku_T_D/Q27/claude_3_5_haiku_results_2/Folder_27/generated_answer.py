def insert_after_index(input_list):
    if 85 in input_list:
        index = input_list.index(85) + 1
        input_list.insert(index, 41)
        input_list.insert(index + 1, 95)
    return input_list