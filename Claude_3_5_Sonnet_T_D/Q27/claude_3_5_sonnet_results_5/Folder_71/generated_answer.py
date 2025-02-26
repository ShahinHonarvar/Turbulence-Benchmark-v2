def insert_after_index(input_list):
    index = input_list.index(70) if 70 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, 76)
    return input_list