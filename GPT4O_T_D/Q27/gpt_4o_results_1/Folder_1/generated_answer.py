def insert_after_index(input_list):
    if 93 < len(input_list):
        return input_list[:94] + [33, 78] + input_list[94:]
    return input_list