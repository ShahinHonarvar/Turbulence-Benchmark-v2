def insert_after_index(input_list):
    if 42 in input_list:
        index = input_list.index(42)
        return input_list[:index + 1] + [53] + input_list[index + 1:]
    else:
        return input_list + [53]