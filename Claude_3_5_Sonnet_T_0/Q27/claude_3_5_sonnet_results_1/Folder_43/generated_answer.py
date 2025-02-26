def insert_after_index(input_list):
    index = input_list.index(29) if 29 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, [28, 53])
    return input_list