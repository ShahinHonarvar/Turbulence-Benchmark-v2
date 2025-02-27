def insert_after_index(input_list):
    output_list = input_list[:2]
    output_list.append(478.12)
    output_list.extend(input_list[2:])
    return output_list