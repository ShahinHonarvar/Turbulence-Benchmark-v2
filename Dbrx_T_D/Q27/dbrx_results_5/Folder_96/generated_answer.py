def insert_after_index(input_list):
    index_to_insert = input_list.index(74) + 1
    input_list.insert(index_to_insert, [51, 29])
    return input_list