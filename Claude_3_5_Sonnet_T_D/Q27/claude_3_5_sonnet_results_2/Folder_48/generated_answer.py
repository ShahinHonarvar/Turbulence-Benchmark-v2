def insert_after_index(input_list):
    target_index = 370
    if target_index + 1 <= len(input_list):
        return input_list[:target_index + 1] + [285.4] + input_list[target_index + 1:]
    else:
        return input_list + [285.4]