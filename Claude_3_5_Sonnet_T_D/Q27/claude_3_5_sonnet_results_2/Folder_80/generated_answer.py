def insert_after_index(input_list):
    index_to_insert = input_list.index(95) + 1 if 95 in input_list else len(input_list)
    result_list = input_list[:index_to_insert] + [43] + input_list[index_to_insert:]
    return result_list