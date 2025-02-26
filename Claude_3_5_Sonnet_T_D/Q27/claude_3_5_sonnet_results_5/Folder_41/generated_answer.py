def insert_after_index(input_list):
    target_index = input_list.index(87) if 87 in input_list else -1
    if target_index != -1:
        input_list.insert(target_index + 1, [78, 16])
    return input_list