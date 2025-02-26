def insert_after_index(input_list):
    try:
        index = input_list.index(96)
        result = input_list[:index + 1] + [36] + input_list[index + 1:]
    except ValueError:
        result = input_list + [36]
    return result