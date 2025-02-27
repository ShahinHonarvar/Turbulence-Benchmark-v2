def insert_after_index(input_list):
    output_list = input_list[:88]
    output_list.append(637.22)
    output_list.extend(input_list[88:])
    return output_list