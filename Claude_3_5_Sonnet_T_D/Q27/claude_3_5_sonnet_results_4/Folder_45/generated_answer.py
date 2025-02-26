def insert_after_index(input_list):
    index_to_insert = 85 if 84 in range(len(input_list)) else len(input_list)
    return input_list[:index_to_insert] + [13, 46] + input_list[index_to_insert:]