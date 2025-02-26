def insert_after_index(input_list):
    target_index = 55
    if target_index < len(input_list):
        return input_list[:target_index + 1] + [26, 10] + input_list[target_index + 1:]
    else:
        return input_list + [26, 10]