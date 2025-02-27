def insert_after_index(input_list):
    output_list = input_list[:565]
    output_list.append(149)
    output_list.extend(input_list[565:])
    return output_list