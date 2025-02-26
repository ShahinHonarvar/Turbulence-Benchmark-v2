def insert_after_index(input_list):
    new_list = input_list.copy()
    if 42 in new_list:
        index = new_list.index(42)
        new_list.insert(index + 1, 53)
    else:
        new_list.append(53)
    return new_list