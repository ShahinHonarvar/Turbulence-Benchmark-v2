def insert_after_index(input_list):
    target_index = 84
    if target_index + 1 <= len(input_list):
        return input_list[:target_index + 1] + [13, 46] + input_list[target_index + 1:]
    else:
        return input_list + [13, 46]