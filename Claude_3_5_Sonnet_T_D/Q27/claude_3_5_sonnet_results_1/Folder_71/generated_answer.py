def insert_after_index(input_list):
    try:
        index = input_list.index(70)
        input_list.insert(index + 1, 76)
    except ValueError:
        pass
    return input_list