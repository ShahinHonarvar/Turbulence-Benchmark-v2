def insert_after_index(input_list):
    index_of_87 = input_list.index(87)
    input_list.insert(index_of_87 + 1, [78, 16])
    return input_list