def insert_after_index(input_list):
    for i, element in enumerate(input_list):
        if element == 96:
            input_list.insert(i + 1, 36)
            break
    return input_list