def insert_after_index(input_list):
    try:
        index = input_list.index(564)
        return input_list[:index + 1] + [149] + input_list[index + 1:]
    except ValueError:
        return input_list + [149]