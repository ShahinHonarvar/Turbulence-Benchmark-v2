def insert_after_index(input_list):
    if 43 in input_list:
        index = input_list.index(43)
        input_list.insert(index + 1, 37)
    return input_list