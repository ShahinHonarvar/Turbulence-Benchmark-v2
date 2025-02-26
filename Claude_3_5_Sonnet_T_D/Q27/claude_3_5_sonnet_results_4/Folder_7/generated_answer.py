def insert_after_index(input_list):
    index_to_insert = input_list.index(323) + 1
    input_list.insert(index_to_insert, [389, 303])
    return input_list