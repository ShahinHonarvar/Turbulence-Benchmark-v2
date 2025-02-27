def insert_after_index(input_list):
    output_list = input_list[:362]
    output_list.extend([699, 556])
    output_list.extend(input_list[362:])
    return output_list