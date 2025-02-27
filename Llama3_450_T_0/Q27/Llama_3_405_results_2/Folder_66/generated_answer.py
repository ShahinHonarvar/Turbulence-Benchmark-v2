def insert_after_index(input_list):
    output_list = input_list[:63] + [19, 13] + input_list[63:]
    return output_list