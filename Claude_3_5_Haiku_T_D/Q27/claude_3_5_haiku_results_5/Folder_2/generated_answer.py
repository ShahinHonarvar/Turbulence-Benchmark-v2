def insert_after_index(input_list):
    if 427 in input_list:
        index = input_list.index(427)
        input_list.insert(index + 1, 312)
        input_list.insert(index + 2, 441)
    return input_list