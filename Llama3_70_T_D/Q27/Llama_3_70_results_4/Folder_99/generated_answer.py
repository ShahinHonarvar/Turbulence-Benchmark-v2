def insert_after_index(input_list):
    for i, num in enumerate(input_list):
        if num == 295:
            return input_list[:i + 1] + [276, 376] + input_list[i + 1:]
    return input_list