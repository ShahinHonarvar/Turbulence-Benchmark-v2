def insert_after_index(input_list):
    try:
        index = input_list.index(70)
        return input_list[:index + 1] + [76] + input_list[index + 1:]
    except ValueError:
        return input_list + [76]