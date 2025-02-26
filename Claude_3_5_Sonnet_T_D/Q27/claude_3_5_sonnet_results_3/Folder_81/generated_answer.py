def insert_after_index(input_list):
    index = 28
    if index < len(input_list):
        return input_list[:index + 1] + [20] + input_list[index + 1:]
    else:
        return input_list + [20]