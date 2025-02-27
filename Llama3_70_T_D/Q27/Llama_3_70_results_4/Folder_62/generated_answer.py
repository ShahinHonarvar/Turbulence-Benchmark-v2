def insert_after_index(input_list):
    output_list = input_list[:36]
    output_list.extend([90, 76])
    output_list.extend(input_list[36:])
    return output_list