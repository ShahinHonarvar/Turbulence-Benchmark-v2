def insert_after_index(input_list):
    index_to_insert = input_list.index(63) + 1 if 63 in input_list else 0
    result_list = input_list[:index_to_insert] + [99] + input_list[index_to_insert:]
    return result_list