def insert_after_index(input_list):
    insert_index = input_list.index(91) + 1
    input_list.insert(insert_index, 46)
    input_list.insert(insert_index + 1, 13)
    return input_list