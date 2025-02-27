def insert_after_index(input_list):
    index_to_insert = input_list.index(91) + 1
    input_list.insert(index_to_insert, 46)
    input_list.insert(index_to_insert + 1, 13)
    return input_list