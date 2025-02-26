def insert_after_index(input_list):
    index_to_insert = input_list.index(7) + 1
    input_list.insert(index_to_insert, [1, 7])
    return input_list