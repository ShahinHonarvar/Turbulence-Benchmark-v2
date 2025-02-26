def insert_after_index(input_list):
    if 42 in input_list:
        index = input_list.index(42)
        input_list.insert(index + 1, 53)
    return input_list