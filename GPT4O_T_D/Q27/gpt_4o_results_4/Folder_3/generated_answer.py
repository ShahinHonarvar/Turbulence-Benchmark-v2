def insert_after_index(input_list):
    modified_list = input_list[:31] + [input_list[31]] + [88, 51] + input_list[32:]
    return modified_list