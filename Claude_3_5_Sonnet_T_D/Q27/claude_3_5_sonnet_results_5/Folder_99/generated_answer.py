def insert_after_index(input_list):
    target_index = input_list.index(295) if 295 in input_list else -1
    if target_index != -1:
        input_list.insert(target_index + 1, [276, 376])
    return input_list