def insert_after_index(input_list):
    output_list = input_list[:52]
    output_list.append(304.62)
    output_list.extend(input_list[52:])
    return output_list