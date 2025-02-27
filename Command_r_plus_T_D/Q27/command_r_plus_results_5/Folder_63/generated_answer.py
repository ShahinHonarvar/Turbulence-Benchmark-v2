def insert_after_index(input_list):
    if 76 < len(input_list):
        input_list.insert(77, 15)
        input_list.insert(78, 51)
    else:
        input_list.append(15)
        input_list.append(51)
    return input_list