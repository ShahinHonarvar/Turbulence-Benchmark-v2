def insert_after_index(input_list):
    if len(input_list) > 31:
        input_list[32:32] = [88, 51]
    return input_list