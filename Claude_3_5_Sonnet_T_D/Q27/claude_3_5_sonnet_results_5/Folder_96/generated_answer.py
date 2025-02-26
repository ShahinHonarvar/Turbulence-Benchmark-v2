def insert_after_index(input_list):
    target_index = input_list.index(74) if 74 in input_list else -1
    new_list = input_list.copy()
    if target_index != -1:
        new_list.insert(target_index + 1, [51, 29])
    return new_list