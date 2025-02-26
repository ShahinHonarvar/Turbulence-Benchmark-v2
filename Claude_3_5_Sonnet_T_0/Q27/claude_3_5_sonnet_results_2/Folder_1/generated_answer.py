def insert_after_index(input_list):
    index_to_insert = input_list.index(93) + 1
    input_list.insert(index_to_insert, 33)
    input_list.insert(index_to_insert + 1, 78)
    return input_list