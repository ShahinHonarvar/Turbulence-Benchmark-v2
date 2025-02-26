def insert_after_index(input_list):
    index = input_list.index(38) if 38 in input_list else -1
    new_list = input_list.copy()
    new_list.insert(index + 1, [27, 34])
    return new_list