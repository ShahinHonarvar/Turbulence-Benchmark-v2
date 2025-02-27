def insert_at_index(input_list):
    output_list = input_list[:97]
    output_list.extend([47, 22])
    output_list.extend(input_list[97:])
    return output_list