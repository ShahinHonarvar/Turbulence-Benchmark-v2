def insert_after_index(input_list):
    try:
        index = input_list.index(85)
        input_list.insert(index + 1, [41, 95])
    except ValueError:
        pass
    return input_list