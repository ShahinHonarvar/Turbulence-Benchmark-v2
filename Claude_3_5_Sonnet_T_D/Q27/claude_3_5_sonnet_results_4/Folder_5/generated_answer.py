def insert_after_index(input_list):
    try:
        index_99 = input_list.index(99)
        return input_list[:index_99 + 1] + [15] + input_list[index_99 + 1:]
    except ValueError:
        return input_list + [15]