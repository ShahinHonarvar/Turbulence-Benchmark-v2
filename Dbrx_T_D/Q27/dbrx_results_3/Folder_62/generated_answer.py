def insert_after_index(input_list):
    for i, item in enumerate(input_list):
        if i == 35:
            return input_list[:i + 1] + [90, 76] + input_list[i + 1:]
    return input_list