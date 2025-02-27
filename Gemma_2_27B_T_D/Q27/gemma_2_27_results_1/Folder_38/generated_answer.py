def insert_after_index(input_list):
    output_list = input_list.copy()
    output_list.insert(input_list.index(89) + 1, 86)
    return output_list