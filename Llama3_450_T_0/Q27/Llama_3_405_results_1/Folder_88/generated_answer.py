def insert_after_index(input_list):
    output_list = input_list[:92] + [46, 13] + input_list[92:]
    return output_list