def insert_after_index(input_list):
    index_to_insert = 58
    result_list = input_list[:index_to_insert] + [76] + input_list[index_to_insert:]
    return result_list