def insert_after_index(input_list):
    index_to_insert = input_list.index(8) + 1
    input_list.insert(index_to_insert, [3, 8])
    return input_list