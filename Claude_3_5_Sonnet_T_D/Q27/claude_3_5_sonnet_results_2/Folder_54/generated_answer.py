def insert_after_index(input_list):
    try:
        index = input_list.index(43)
        input_list.insert(index + 1, 37)
    except ValueError:
        pass
    return input_list