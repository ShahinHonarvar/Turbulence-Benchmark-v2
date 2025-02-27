def insert_after_index(input_list):
    output_list = input_list[:56] + [[26, 10]] + input_list[56:]
    return output_list