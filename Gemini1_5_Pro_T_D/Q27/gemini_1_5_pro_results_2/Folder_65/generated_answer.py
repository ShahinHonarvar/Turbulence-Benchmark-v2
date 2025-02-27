def insert_after_index(input_list):
    output_list = input_list[:71]
    output_list.append(185.43)
    output_list.extend(input_list[71:])
    return output_list