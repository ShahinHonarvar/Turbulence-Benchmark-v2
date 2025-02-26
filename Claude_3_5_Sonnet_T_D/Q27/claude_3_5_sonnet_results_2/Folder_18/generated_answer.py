def insert_after_index(input_list):
    target_index = 696
    if target_index < len(input_list):
        return input_list[:target_index + 1] + [477] + input_list[target_index + 1:]
    else:
        return input_list + [477]