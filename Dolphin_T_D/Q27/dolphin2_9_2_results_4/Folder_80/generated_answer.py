def insert_after_index(input_list):
    if 95 in range(len(input_list)):
        input_list.insert(input_list.index(95) + 1, 43)
    else:
        input_list.append(43)
    return input_list