def insert_after_index(input_list):
    new_list = input_list.copy()
    if len(new_list) > 92:
        new_list.insert(93, 709.87)
    else:
        new_list.append(709.87)
    return new_list