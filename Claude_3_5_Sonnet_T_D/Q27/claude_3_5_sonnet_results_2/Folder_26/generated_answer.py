def insert_after_index(input_list):
    index_to_insert = input_list.index(55) + 1
    input_list.insert(index_to_insert, [26, 10])
    return input_list