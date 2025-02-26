def insert_after_index(input_list):
    try:
        index = input_list.index(62)
        input_list.insert(index + 1, 51)
    except ValueError:
        pass
    return input_list