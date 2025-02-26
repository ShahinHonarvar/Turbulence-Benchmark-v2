def insert_after_index(input_list):
    target_index = 91
    if target_index < len(input_list):
        return input_list[:target_index + 1] + [46, 13] + input_list[target_index + 1:]
    else:
        return input_list + [46, 13]