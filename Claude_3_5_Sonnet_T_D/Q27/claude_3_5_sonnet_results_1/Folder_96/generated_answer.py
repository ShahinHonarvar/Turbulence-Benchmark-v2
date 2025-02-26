def insert_after_index(input_list):
    target_index = input_list.index(74) if 74 in input_list else -1
    if target_index != -1:
        input_list.insert(target_index + 1, [51, 29])
    return input_list