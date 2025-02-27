def insert_after_index(input_list):
    for i in range(len(input_list)):
        if input_list[i] == 99:
            input_list.insert(i + 1, 99)
            return input_list
    return input_list + [99]