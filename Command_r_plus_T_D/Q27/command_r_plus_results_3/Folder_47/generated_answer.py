def insert_after_index(input_list):
    if len(input_list) > 64:
        input_list.insert(65, 520.11)
    elif len(input_list) == 64:
        input_list.append(520.11)
    return input_list