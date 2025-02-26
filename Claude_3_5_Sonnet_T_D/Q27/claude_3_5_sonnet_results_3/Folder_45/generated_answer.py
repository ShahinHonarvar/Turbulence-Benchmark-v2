def insert_after_index(input_list):
    new_list = input_list.copy()
    target_index = 84
    if target_index + 1 < len(new_list):
        new_list.insert(target_index + 1, [13, 46])
    else:
        new_list.append([13, 46])
    return new_list