def insert_after_index(input_list):
    if len(input_list) > 70:
        input_list.insert(71, 185.43)
    else:
        input_list.append(185.43)
    return input_list