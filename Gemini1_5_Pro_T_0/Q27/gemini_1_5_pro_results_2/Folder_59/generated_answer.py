def insert_after_index(input_list):
    output_list = input_list[:10]
    output_list.append(426.08)
    output_list.extend(input_list[10:])
    return output_list