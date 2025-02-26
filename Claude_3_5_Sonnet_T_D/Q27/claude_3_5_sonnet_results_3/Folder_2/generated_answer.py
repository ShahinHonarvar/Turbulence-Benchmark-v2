def insert_after_index(input_list):
    try:
        index = input_list.index(427)
        return input_list[:index + 1] + [312, 441] + input_list[index + 1:]
    except ValueError:
        return input_list + [312, 441]