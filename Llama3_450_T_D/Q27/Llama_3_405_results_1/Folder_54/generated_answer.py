def insert_after_index(input_list):
    if 43 in input_list:
        index = input_list.index(43)
        return input_list[:index + 1] + [37] + input_list[index + 1:]
    else:
        return input_list