def insert_after_index(input_list):
    index = input_list.index(7) if 7 in input_list else -1
    new_list = input_list.copy()
    new_list.insert(index + 1, [1, 7])
    return new_list