def insert_after_index(input_list):
    if len(input_list) > 20:
        input_list.insert(21, 80)
    else:
        input_list.append(80)
    return input_list