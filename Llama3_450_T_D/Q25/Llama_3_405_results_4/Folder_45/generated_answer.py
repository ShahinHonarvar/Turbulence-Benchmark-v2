def insert_at_index(input_list):
    output_list = input_list[:84] + [[13, 46]] + input_list[84:]
    return output_list