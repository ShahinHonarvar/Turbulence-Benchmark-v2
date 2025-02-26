def insert_after_index(input_list):
    target_index = input_list.index(8) if 8 in input_list else -1
    if target_index != -1:
        input_list.insert(target_index + 1, [3, 8])
    return input_list