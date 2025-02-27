def insert_after_index(input_list):
    if len(input_list) > 15:
        input_list.insert(16, 550.97)
    else:
        input_list.append(550.97)
    return input_list