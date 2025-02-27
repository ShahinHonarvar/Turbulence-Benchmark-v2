def insert_after_index(input_list):
    output_list = input_list.copy()
    index = output_list.index(56) if 56 in output_list else len(output_list)
    output_list.insert(index + 1, 54)
    return output_list