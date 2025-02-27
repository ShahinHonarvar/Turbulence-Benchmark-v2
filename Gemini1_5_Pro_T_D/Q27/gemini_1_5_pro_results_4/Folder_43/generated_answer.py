def insert_after_index(input_list):
    output_list = input_list[:30]
    output_list.extend([28, 53])
    output_list.extend(input_list[30:])
    return output_list