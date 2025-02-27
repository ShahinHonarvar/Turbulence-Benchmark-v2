def insert_after_index(input_list):
    try:
        index = input_list.index(983)
        return input_list[:index + 1] + [369] + input_list[index + 1:]
    except ValueError:
        return input_list