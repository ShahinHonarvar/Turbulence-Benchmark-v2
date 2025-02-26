def insert_after_index(input_list):
    index = 8
    if index + 1 <= len(input_list):
        return input_list[:index + 1] + [3, 8] + input_list[index + 1:]
    else:
        return input_list + [3, 8]