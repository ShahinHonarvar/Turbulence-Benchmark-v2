def insert_after_index(input_list):
    index = input_list.index(85) if 85 in input_list else -1
    if index != -1:
        input_list.insert(index + 1, [41, 95])
    else:
        input_list.append([41, 95])
    return input_list