def insert_after_index(input_list):
    if len(input_list) > 49:
        return input_list[:50] + [0.78] + input_list[50:]
    return input_list + [0.78]