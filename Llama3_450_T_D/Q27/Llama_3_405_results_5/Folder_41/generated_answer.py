def insert_after_index(input_list):
    index = 87
    if index < len(input_list):
        return input_list[:index + 1] + [78, 16] + input_list[index + 1:]
    else:
        return input_list + [78, 16]