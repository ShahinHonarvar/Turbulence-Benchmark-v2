def insert_after_index(input_list):
    insert_index = input_list.index(990) + 1
    input_list.insert(insert_index, 905)
    input_list.insert(insert_index + 1, 742)
    return input_list