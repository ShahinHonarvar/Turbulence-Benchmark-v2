def insert_after_index(input_list):
    index = input_list.index(427) if 427 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, [312, 441])
    return input_list