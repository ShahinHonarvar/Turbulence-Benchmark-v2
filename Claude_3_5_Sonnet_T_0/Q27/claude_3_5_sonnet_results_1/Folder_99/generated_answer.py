def insert_after_index(input_list):
    index = input_list.index(295) if 295 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, 276)
        input_list.insert(index + 2, 376)
    return input_list