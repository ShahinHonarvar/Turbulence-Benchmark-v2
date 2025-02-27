def insert_after_index(input_list):
    output_list = input_list[:85]
    output_list.append(771.92)
    output_list.extend(input_list[85:])
    return output_list