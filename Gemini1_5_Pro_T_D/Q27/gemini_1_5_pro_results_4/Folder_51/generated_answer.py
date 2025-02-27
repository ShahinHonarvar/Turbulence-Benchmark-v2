def insert_after_index(input_list):
    output_list = input_list[:20]
    output_list.append(249.61)
    output_list.extend(input_list[20:])
    return output_list