def insert_after_index(input_list):
    output_list = input_list[:98]
    output_list.append(72.27)
    output_list.extend(input_list[98:])
    return output_list