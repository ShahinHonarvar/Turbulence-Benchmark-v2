def insert_after_index(input_list):
    if 99 in input_list:
        index = input_list.index(99)
        input_list.insert(index + 1, 99)
    return input_list