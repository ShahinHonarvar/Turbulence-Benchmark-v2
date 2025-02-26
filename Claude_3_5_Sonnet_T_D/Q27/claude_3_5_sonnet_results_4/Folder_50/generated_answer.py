def insert_after_index(input_list):
    index = input_list.index(52) if 52 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, 38)
    return input_list