def insert_after_index(input_list):
    index_to_insert = 63
    new_list = input_list[:index_to_insert] + [19, 13] + input_list[index_to_insert:]
    return new_list