def insert_after_index(input_list):
    for i, item in enumerate(input_list):
        if item == 93:
            return input_list[:i + 1] + [33, 78] + input_list[i + 1:]
    return input_list + [33, 78]