def insert_after_index(input_list):
    new_list = input_list.copy()
    if 57 < len(new_list):
        new_list.insert(58, 76)
    else:
        new_list.append(76)
    return new_list