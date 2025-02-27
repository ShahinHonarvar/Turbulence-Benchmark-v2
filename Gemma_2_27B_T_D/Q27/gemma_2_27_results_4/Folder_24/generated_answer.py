def insert_after_index(input_list):
    output_list = input_list[:]
    output_list.insert(input_list.index(42) + 1, 53)
    return output_list