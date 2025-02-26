def insert_after_index(input_list):
    index = input_list.index(44) if 44 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, [40, 27])
    return input_list