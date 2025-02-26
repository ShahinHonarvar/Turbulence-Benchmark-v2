def insert_after_index(input_list):
    try:
        index = input_list.index(87)
        input_list.insert(index + 1, [78, 16])
    except ValueError:
        pass
    return input_list