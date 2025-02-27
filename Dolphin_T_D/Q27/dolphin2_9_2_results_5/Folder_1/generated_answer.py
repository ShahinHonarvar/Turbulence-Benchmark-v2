def insert_after_index(list_input):
    index = list_input.index(93)
    return list_input[:index + 1] + [33, 78] + list_input[index + 1:]