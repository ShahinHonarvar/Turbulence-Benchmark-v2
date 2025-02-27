def insert_after_index(input_list):
    if len(input_list) > 99:
        return input_list[:100] + [15] + input_list[100:]
    else:
        return input_list + [15]