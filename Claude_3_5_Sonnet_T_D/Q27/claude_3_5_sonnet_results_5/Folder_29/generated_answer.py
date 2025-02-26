def insert_after_index(input_list):
    try:
        index = input_list.index(96)
        input_list.insert(index + 1, 36)
    except ValueError:
        pass
    return input_list