def insert_after_index(input_list):
    try:
        index = input_list.index(93)
        return input_list[:index + 1] + [33, 78] + input_list[index + 1:]
    except ValueError:
        return input_list + [33, 78]