def insert_after_index(input_list):
    target_index = 97
    if target_index + 1 <= len(input_list):
        return input_list[:target_index + 1] + [47, 22] + input_list[target_index + 1:]
    else:
        return input_list + [47, 22]