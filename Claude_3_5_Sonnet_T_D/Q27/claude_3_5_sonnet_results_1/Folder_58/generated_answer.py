def insert_after_index(input_list):
    target_index = 598
    if target_index + 1 <= len(input_list):
        return input_list[:target_index + 1] + [385, 999] + input_list[target_index + 1:]
    else:
        return input_list + [385, 999]