def insert_after_index(input_list):
    try:
        index = input_list.index(99)
        result_list = input_list[:index + 1] + [15] + input_list[index + 1:]
    except ValueError:
        result_list = input_list + [15]
    return result_list