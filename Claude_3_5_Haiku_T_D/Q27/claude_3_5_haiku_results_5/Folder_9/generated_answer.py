def insert_after_index(input_list):
    if 66 in input_list:
        index = input_list.index(66)
        input_list.insert(index + 1, 45)
    return input_list