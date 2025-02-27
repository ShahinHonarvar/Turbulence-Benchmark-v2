def insert_after_index(input_list):
    output_list = input_list[:371]
    output_list.append(285.4)
    output_list.extend(input_list[371:])
    return output_list