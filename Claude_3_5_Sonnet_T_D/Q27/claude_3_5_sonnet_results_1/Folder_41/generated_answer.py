def insert_after_index(input_list):
    index_87 = input_list.index(87) if 87 in input_list else -1
    if index_87 != -1:
        input_list.insert(index_87 + 1, [78, 16])
    return input_list