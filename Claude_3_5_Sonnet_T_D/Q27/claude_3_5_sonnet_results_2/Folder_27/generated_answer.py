def insert_after_index(input_list):
    target_index = input_list.index(85) if 85 in input_list else -1
    if target_index != -1:
        input_list.insert(target_index + 1, [41, 95])
    return input_list