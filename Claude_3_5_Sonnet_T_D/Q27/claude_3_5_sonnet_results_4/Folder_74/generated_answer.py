def insert_after_index(input_list):
    index = 41
    if index < len(input_list):
        return input_list[:index + 1] + [74, 70] + input_list[index + 1:]
    else:
        return input_list + [74, 70]