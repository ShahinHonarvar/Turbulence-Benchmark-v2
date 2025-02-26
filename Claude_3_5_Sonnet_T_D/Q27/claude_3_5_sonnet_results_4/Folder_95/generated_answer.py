def insert_after_index(input_list):
    target_index = 20
    if target_index < len(input_list):
        return input_list[:target_index + 1] + [80] + input_list[target_index + 1:]
    else:
        return input_list + [80]