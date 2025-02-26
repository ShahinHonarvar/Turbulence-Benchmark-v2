def insert_after_index(input_list):
    target_index = 183
    if target_index + 1 <= len(input_list):
        return input_list[:target_index + 1] + [148, 145] + input_list[target_index + 1:]
    else:
        return input_list + [148, 145]