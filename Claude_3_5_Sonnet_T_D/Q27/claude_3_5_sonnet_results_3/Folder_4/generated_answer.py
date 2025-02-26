def insert_after_index(input_list):
    index = input_list.index(60) if 60 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, [80, 74])
    return input_list