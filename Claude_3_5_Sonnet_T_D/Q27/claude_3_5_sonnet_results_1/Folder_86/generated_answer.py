def insert_after_index(input_list):
    target_index = 990
    if target_index < len(input_list):
        return input_list[:target_index + 1] + [905, 742] + input_list[target_index + 1:]
    else:
        return input_list + [905, 742]