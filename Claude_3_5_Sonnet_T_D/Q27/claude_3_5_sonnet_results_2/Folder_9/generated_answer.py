def insert_after_index(input_list):
    try:
        index = input_list.index(66)
        input_list.insert(index + 1, 45)
    except ValueError:
        pass
    return input_list