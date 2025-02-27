def insert_after_index(input_list):
    output_list = input_list[:77]
    output_list.append(10.01)
    output_list.extend(input_list[77:])
    return output_list