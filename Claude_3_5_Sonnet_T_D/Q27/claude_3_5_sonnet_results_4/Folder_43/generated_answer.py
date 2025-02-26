def insert_after_index(input_list):
    index = 29
    if index < len(input_list):
        return input_list[:index + 1] + [28, 53] + input_list[index + 1:]
    else:
        return input_list + [28, 53]