def insert_after_index(input_list):
    output_list = input_list[:29]
    output_list.append(717.02)
    output_list.extend(input_list[29:])
    return output_list