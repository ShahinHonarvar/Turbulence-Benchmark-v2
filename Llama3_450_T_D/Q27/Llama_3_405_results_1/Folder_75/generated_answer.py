def insert_after_index(input_list):
    if 99 in input_list:
        index = input_list.index(99)
        return input_list[:index + 1] + [99] + input_list[index + 1:]
    else:
        return input_list