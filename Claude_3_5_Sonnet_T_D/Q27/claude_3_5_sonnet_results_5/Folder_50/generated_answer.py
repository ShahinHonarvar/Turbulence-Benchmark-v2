def insert_after_index(input_list):
    new_list = input_list.copy()
    try:
        index = input_list.index(52)
        new_list.insert(index + 1, 38)
    except ValueError:
        pass
    return new_list