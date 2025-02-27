def insert_after_index(input_list):
    for i in range(len(input_list)):
        if input_list[i] == 44:
            input_list.insert(i + 1, 76)
            break
    return input_list