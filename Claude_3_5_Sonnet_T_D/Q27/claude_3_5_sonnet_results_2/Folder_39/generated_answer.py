def insert_after_index(input_list):
    new_list = input_list.copy()
    target_index = 97
    if target_index + 1 < len(new_list):
        new_list.insert(target_index + 1, [47, 22])
    else:
        new_list.append([47, 22])
    return new_list