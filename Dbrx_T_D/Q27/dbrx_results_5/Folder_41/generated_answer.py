def insert_after_index(input_list):
    for i, item in enumerate(input_list):
        if item == 87:
            return input_list[:i + 1] + [78, 16] + input_list[i + 1:]
    return input_list + [78, 16]