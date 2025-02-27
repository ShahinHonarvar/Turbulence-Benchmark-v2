def insert_after_index(input_list):
    output_list = input_list[:93]
    output_list.append(709.87)
    output_list += input_list[93:]
    return output_list