def insert_after_index(input_list):
    try:
        index = input_list.index(38)
        input_list.insert(index + 1, [27, 34])
    except ValueError:
        pass
    return input_list