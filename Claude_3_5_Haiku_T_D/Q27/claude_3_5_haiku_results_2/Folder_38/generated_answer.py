def insert_after_index(input_list):
    if 89 in input_list:
        idx = input_list.index(89)
        input_list.insert(idx + 1, 86)
    return input_list