def insert_after_index(input_list):
    target_index = 76
    if target_index < len(input_list):
        return input_list[:target_index + 1] + [15, 51] + input_list[target_index + 1:]
    else:
        return input_list + [15, 51]