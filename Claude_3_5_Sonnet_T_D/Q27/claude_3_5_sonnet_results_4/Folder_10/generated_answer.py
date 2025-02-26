def insert_after_index(input_list):
    try:
        index = input_list.index(56)
        input_list.insert(index + 1, 54)
    except ValueError:
        pass
    return input_list