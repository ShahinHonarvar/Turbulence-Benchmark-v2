def insert_after_index(input_list):
    output_list = input_list[:22]
    output_list.append(655.24)
    output_list.extend(input_list[22:])
    return output_list