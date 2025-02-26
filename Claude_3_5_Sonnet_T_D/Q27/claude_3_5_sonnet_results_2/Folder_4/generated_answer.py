def insert_after_index(input_list):
    index_to_insert = input_list.index(60) + 1
    return input_list[:index_to_insert] + [80, 74] + input_list[index_to_insert:]