def insert_after_index(input_list):
    index_to_insert = input_list.index(990) + 1
    input_list.insert(index_to_insert, [905, 742])
    return input_list