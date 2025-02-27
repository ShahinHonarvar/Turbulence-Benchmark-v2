def insert_after_index(input_list):
    output_list = input_list[:32] + [88, 51] + input_list[32:]
    return output_list