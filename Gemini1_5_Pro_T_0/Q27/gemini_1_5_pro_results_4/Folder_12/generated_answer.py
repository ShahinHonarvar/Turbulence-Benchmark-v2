def insert_after_index(input_list):
    output_list = input_list[:58]
    output_list.append(96)
    output_list.extend(input_list[58:])
    return output_list